#!/usr/bin/env python3
"""Coleta paginada; janela de dias UTC completos [end-days, end)."""
import argparse
import calendar
from datetime import date, datetime, timedelta, timezone
import hashlib
import html
from html.parser import HTMLParser
import json
import logging
import os
from pathlib import Path
import re
import time
from urllib.parse import quote, urlparse, urljoin
import xml.etree.ElementTree as ET

import feedparser
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import yaml

ROOT = Path(__file__).resolve().parents[1]
ATOM = {'a': 'http://www.w3.org/2005/Atom', 'o': 'http://a9.com/-/spec/opensearch/1.1/',
        'x': 'http://arxiv.org/schemas/atom'}


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(text, encoding='utf-8')
    tmp.replace(path)


def markdown(text):
    # Metadados externos nunca podem inserir HTML, imagens ou links Markdown.
    return re.sub(r'([\\`*_{}\[\]()#+.!|>~-])', r'\\\1', html.escape(str(text))).replace('\n', ' ')


def frontmatter(meta, body):
    return '---\n' + yaml.safe_dump(meta, allow_unicode=True, sort_keys=False) + '---\n\n' + body


def read_note(path):
    lines = path.read_text(encoding='utf-8').splitlines()
    if not lines or lines[0] != '---':
        raise ValueError(f'Frontmatter ausente em {path.name}')
    closing = lines.index('---', 1)
    return yaml.safe_load('\n'.join(lines[1:closing]))


def doi(value):
    value = re.sub(r'^https?://(?:dx\.)?doi.org/', '', value or '', flags=re.I)
    return value.strip().lower() or None


def safe_url(value):
    return value if value and urlparse(value).scheme in ('http', 'https') else ''


def inverted_abstract(index):
    if not index:
        return ''
    return ' '.join(word for _, word in sorted((p, w) for w, ps in index.items() for p in ps))


def openalex_record(w, category):
    d = doi(w.get('doi'))
    return dict(title=w.get('title') or 'Sem título',
                authors=[a['author']['display_name'] for a in w.get('authorships', [])],
                date=w['publication_date'], type=w['type'], category=[category], doi=d,
                abstract=inverted_abstract(w.get('abstract_inverted_index')),
                source=['OpenAlex'], source_ids=[w['id']],
                url='https://doi.org/' + quote(d, safe='/') if d else w['id'])


def arxiv_records(xml, category):
    root = ET.fromstring(xml)
    entries = root.findall('a:entry', ATOM)
    if any(e.findtext('a:title', '', ATOM).lower().strip() == 'error' for e in entries):
        raise RuntimeError('arXiv retornou erro na consulta')
    records = []
    for e in entries:
        identifier = re.sub(r'v\d+$', '', e.findtext('a:id', '', ATOM).split('/abs/')[-1])
        records.append(dict(title=' '.join(e.findtext('a:title', '', ATOM).split()),
            authors=[a.findtext('a:name', '', ATOM) for a in e.findall('a:author', ATOM)],
            date=e.findtext('a:published', '', ATOM)[:10], type='preprint', category=[category],
            doi=doi(e.findtext('x:doi', '', ATOM)),
            abstract=' '.join(e.findtext('a:summary', '', ATOM).split()),
            source=['arXiv'], source_ids=['arxiv:' + identifier],
            url='https://arxiv.org/abs/' + quote(identifier, safe='/')))
    total = root.findtext('o:totalResults', None, ATOM)
    if total is None:
        raise RuntimeError('Resposta arXiv sem totalResults')
    return records, int(total)


class FeedHTML(HTMLParser):
    """Extrai texto e links RSS anunciados pelo próprio PhilPapers."""
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.text = []
        self.feeds = set()
        self.hidden = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in ('script', 'style'):
            self.hidden += 1
        href = attrs.get('href', '')
        if tag in ('link', 'a') and href:
            mime = attrs.get('type', '').split(';')[0].lower()
            if mime in ('application/rss+xml', 'application/atom+xml') or re.search(r'(?:/rss(?:[/.?]|$)|rss\.pl|[?&]format=rss(?:&|$))', href, re.I):
                self.feeds.add(href)
        if tag in ('p', 'br', 'div', 'li'):
            self.text.append(' ')

    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self.hidden = max(0, self.hidden - 1)
        self.text.append(' ')

    def handle_data(self, data):
        if not self.hidden:
            self.text.append(data)


def feed_text(value):
    parser = FeedHTML()
    parser.feed(value or '')
    return ' '.join(''.join(parser.text).split())


def philpapers_url(url):
    parsed = urlparse(url)
    if parsed.scheme != 'https' or parsed.hostname not in ('philpapers.org', 'www.philpapers.org'):
        raise RuntimeError('Configure uma URL HTTPS do PhilPapers em topics.yml')
    return url


def discover_philpapers_feed(client, page_url):
    page_url = philpapers_url(page_url)
    response = client.get(page_url, {})
    parser = FeedHTML()
    parser.feed(response.text)
    candidates = {urljoin(page_url, href) for href in parser.feeds}
    candidates = {u for u in candidates if urlparse(u).hostname in ('philpapers.org', 'www.philpapers.org')}
    if len(candidates) != 1:
        raise RuntimeError('Não foi possível identificar um único RSS da categoria PhilPapers. '
                           'Copie o endereço do RSS da categoria para feed_url em topics.yml.')
    return philpapers_url(candidates.pop())


def philpapers_records(content, category, start, end, observed_on=None):
    feed = feedparser.parse(content)
    if feed.bozo or not feed.version:
        raise RuntimeError('PhilPapers retornou um feed RSS/Atom inválido')
    observed_on = observed_on or datetime.now(timezone.utc).date()
    records = []
    for entry in feed.entries:
        stamp = entry.get('published_parsed') or entry.get('updated_parsed')
        basis = 'feed_published' if entry.get('published_parsed') else 'feed_updated'
        if stamp:
            day = datetime.fromtimestamp(calendar.timegm(stamp), timezone.utc).date()
            if not start <= day < end:
                continue
        else:
            # RSS pode omitir datas. Incluir alertas ainda disponíveis e deduplicar.
            day, basis = observed_on, 'discovered'
        link = safe_url(entry.get('link', ''))
        if not link or not entry.get('title'):
            raise RuntimeError('Item PhilPapers sem título ou link; coleta interrompida')
        identifier = entry.get('id') or link
        # Links da mesma ficha podem vir com query string ou protocolos diferentes.
        match = re.search(r'philpapers\.org/rec/([^/?#]+)', link, re.I)
        if match:
            identifier = 'https://philpapers.org/rec/' + match.group(1)
            link = identifier
        candidates = [entry.get('prism_doi', ''), entry.get('doi', ''), entry.get('dc_identifier', ''), entry.get('id', '')]
        candidates += [v.get('href', '') for v in entry.get('links', [])]
        d = None
        for candidate in candidates:
            candidate = doi(re.sub(r'^doi:\s*', '', str(candidate), flags=re.I))
            if candidate and re.fullmatch(r'10\.\d{4,9}/\S+', candidate):
                d = candidate
                break
        authors = [feed_text(a['name']) for a in entry.get('authors', []) if a.get('name')]
        if not authors and entry.get('author'):
            authors = [feed_text(entry['author'])]
        # Descrição RSS pode ser uma referência, não necessariamente um abstract.
        summary = feed_text(entry.get('summary', ''))
        records.append(dict(title=feed_text(entry['title']), authors=authors, date=day.isoformat(),
                            type='unknown', category=[category], doi=d, abstract=summary,
                            abstract_basis='feed_summary' if summary else 'unavailable', date_basis=basis,
                            source=['PhilPapers'], source_ids=['philpapers:' + identifier], url=link))
    return records


def collect_philpapers(client, config, start, end):
    records = []
    for settings in config.get('philpapers', []):
        url = settings.get('feed_url') or discover_philpapers_feed(client, settings['page_url'])
        response = client.get(philpapers_url(url), {})
        records.extend(philpapers_records(response.content, settings['category'], start, end))
    return records


class Client:
    def __init__(self, contact):
        logging.getLogger('urllib3.connectionpool').setLevel(logging.ERROR)
        self.s = requests.Session()
        self.s.headers['User-Agent'] = f'MenteSemanal/1.0 (mailto:{contact})'
        retry = Retry(total=5, backoff_factor=2, status_forcelist=[429, 500, 502, 503, 504],
                      allowed_methods=['GET'], respect_retry_after_header=True)
        self.s.mount('https://', HTTPAdapter(max_retries=retry))
        self.last_arxiv = 0

    def get(self, url, params):
        if 'arxiv.org' in url:
            time.sleep(max(0, 3.2 - (time.monotonic() - self.last_arxiv)))
            self.last_arxiv = time.monotonic()
        r = self.s.get(url, params=params, timeout=(15, 90))
        # Não imprimir URL: ela contém a chave OpenAlex.
        if not r.ok:
            raise RuntimeError(f'Falha HTTP {r.status_code} em {urlparse(url).hostname}')
        return r


def collect_openalex(client, term, category, start, end, key, limit):
    """Pagina [start, end); divide janelas grandes, sem truncar resultados."""
    records = []
    cursor, seen, count = '*', set(), 0
    until = end - timedelta(days=1)
    while cursor:
        if cursor in seen:
            raise RuntimeError('Cursor repetido no OpenAlex')
        seen.add(cursor)
        data = client.get('https://api.openalex.org/works', dict(
            search=term,
            filter=f'from_publication_date:{start},to_publication_date:{until},type:article|book|dissertation',
            cursor=cursor, per_page=200, api_key=key)).json()
        total = data['meta']['count']
        if total > limit:
            days = (end - start).days
            if days <= 1:
                raise RuntimeError(f'OpenAlex: {category} tem {total} resultados no dia {start}; '
                                   f'refine a busca ou aumente max_results_per_query (atual: {limit}).')
            middle = start + timedelta(days=days // 2)
            print(f'OpenAlex: dividindo janela de {category} ({start} até {end}, fim exclusivo); '
                  f'{total} resultados.')
            return (collect_openalex(client, term, category, start, middle, key, limit) +
                    collect_openalex(client, term, category, middle, end, key, limit))
        batch = data['results']
        records.extend(openalex_record(w, category) for w in batch)
        count += len(batch)
        if count > limit:
            raise RuntimeError('OpenAlex excedeu o limite durante a paginação; tente novamente.')
        cursor = data['meta'].get('next_cursor') if batch else None
    return records


def collect(client, config, start, end):
    records = []
    key = os.environ.get('OPENALEX_API_KEY')
    if not key:
        raise RuntimeError('Defina OPENALEX_API_KEY (chave gratuita da conta OpenAlex).')
    until = end - timedelta(days=1)
    limit = config.get('max_results_per_query', 5000)
    if not isinstance(limit, int) or isinstance(limit, bool) or limit < 1:
        raise ValueError('max_results_per_query deve ser um inteiro positivo')
    for category, queries in config['categories'].items():
        for term in queries['openalex']:
            records.extend(collect_openalex(client, term, category, start, end, key, limit))
        offset = 0
        # O último minuto do dia anterior mantém o intervalo sem sobreposição.
        query = f"({queries['arxiv']}) AND submittedDate:[{start:%Y%m%d}0000 TO {until:%Y%m%d}2359]"
        while True:
            batch, total = arxiv_records(client.get('https://export.arxiv.org/api/query', dict(
                search_query=query, start=offset, max_results=200,
                sortBy='submittedDate', sortOrder='ascending')).content, category)
            if total > limit or total > 10000:
                raise RuntimeError(f'arXiv: refine a busca de {category}; {total} resultados')
            if not batch and offset < total:
                raise RuntimeError('arXiv retornou página vazia antes do fim')
            records.extend(batch)
            offset += len(batch)
            if offset >= total:
                break
    records.extend(collect_philpapers(client, config, start, end))
    return records


def aliases(r):
    keys = set(r['source_ids'])
    if r.get('doi'):
        keys.add('doi:' + doi(r['doi']))
    # Título + primeiro autor, conservador: não unir apenas por título.
    norm = lambda x: re.sub(r'\W+', '', x.casefold())
    if r.get('authors'):
        keys.add('title:' + norm(r['title']) + ':' + norm(r['authors'][0]))
    return keys


def save_records(records, root):
    directory = root / 'docs/publications'
    notes = {p.stem: read_note(p) for p in directory.glob('*.md')}
    lookup = {a: k for k, r in notes.items() for a in aliases(r)}
    new_ids = []
    for r in records:
        keys = aliases(r)
        matches = sorted({lookup[a] for a in keys if a in lookup})
        if len(matches) > 1:
            raise RuntimeError('Identidades ambíguas; revise os registros antes de continuar')
        uid = matches[0] if matches else hashlib.sha256(sorted(keys)[0].encode()).hexdigest()[:20]
        if uid in notes:
            old = notes[uid]
            for field in ('category', 'source', 'source_ids'):
                old[field] = sorted(set(old[field]) | set(r[field]))
            if not old.get('abstract') or (old.get('abstract_basis') == 'feed_summary' and r.get('abstract') and not r.get('abstract_basis')):
                old['abstract'] = r['abstract']
                old.pop('abstract_basis', None)
                if r.get('abstract_basis'):
                    old['abstract_basis'] = r['abstract_basis']
            if old.get('type') == 'unknown' and r['type'] != 'unknown':
                old['type'] = r['type']
            if not old.get('authors'):
                old['authors'] = r['authors']
            if old.get('date_basis') and not r.get('date_basis'):
                old['date'] = r['date']
                old.pop('date_basis', None)
            if not old.get('doi'):
                old['doi'] = r['doi']
            r = old
        else:
            r['discovered_at'] = datetime.now(timezone.utc).date().isoformat()
            new_ids.append(uid)
        notes[uid] = r
        for a in aliases(r):
            lookup[a] = uid
    # Só gravar depois de toda a validação e coleta.
    for uid, r in notes.items():
        r['tags'] = r['category']
        source = safe_url(r['url'])
        date_label = {'discovered': 'Data de descoberta', 'feed_published': 'Data do alerta no feed',
                      'feed_updated': 'Atualização do alerta no feed'}.get(r.get('date_basis'), 'Data')
        summary_label = 'Descrição do feed' if r.get('abstract_basis') == 'feed_summary' else 'Resumo'
        body = (f"# {markdown(r['title'])}\n\n"
                f"**Autores:** {markdown('; '.join(r['authors']))}\n\n"
                f"**{date_label}:** {r['date']} · **Tipo:** {r['type']}\n\n"
                f"## {summary_label}\n\n{markdown(r['abstract'] or 'Resumo indisponível na fonte.')}\n\n"
                f"[Consultar publicação](<{source}>)\n")
        write(directory / f'{uid}.md', frontmatter(r, body))
    return new_ids


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--days', type=int, default=7)
    parser.add_argument('--end', type=date.fromisoformat, default=datetime.now(timezone.utc).date())
    args = parser.parse_args()
    if args.days < 1:
        parser.error('--days deve ser positivo')
    config = yaml.safe_load((ROOT / 'topics.yml').read_text())
    contact = os.environ.get('CONTACT_EMAIL', '')
    if '@' not in contact:
        raise SystemExit('Defina CONTACT_EMAIL com um contato válido para as APIs.')
    start = args.end - timedelta(days=args.days)
    try:
        records = collect(Client(contact), config, start, args.end)
    except requests.RequestException:
        raise SystemExit('Falha de rede; nenhuma edição foi gravada. Consulte as APIs sem expor a chave.')
    ids = save_records(records, ROOT)
    manifest = ROOT / f'data/editions/{args.end}.json'
    old = json.loads(manifest.read_text()) if manifest.exists() else {}
    edition = dict(date=str(args.end), start=str(start), end_exclusive=str(args.end),
                   ids=sorted(set(old.get('ids', [])) | set(ids)))
    write(manifest, json.dumps(edition, ensure_ascii=False, indent=2) + '\n')
    print(f'{len(records)} ocorrências; {len(ids)} publicações novas; edição {args.end}.')


if __name__ == '__main__':
    main()
