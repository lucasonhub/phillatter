"""Seleciona uma edição de dez artigos por semana, sem filtro de data bibliográfica."""
import argparse
from copy import deepcopy
from datetime import date, datetime, timedelta
import json
import os
from pathlib import Path
import re
import unicodedata
import xml.etree.ElementTree as ET
from zoneinfo import ZoneInfo

import requests
import yaml
from collect import (ROOT, Client, aliases, arxiv_records, doi, download_philpapers_feed,
                     discover_philpapers_feed, openalex_record, philpapers_records,
                     read_note, save_records, write)


def normalized(value):
    return ''.join(c for c in unicodedata.normalize('NFKD', str(value).casefold())
                   if not unicodedata.combining(c))


def contains(text, phrase):
    return re.search(r'(?<!\w)' + re.escape(normalized(phrase)) + r'(?!\w)', text) is not None


def relevance(record, profile):
    title = normalized(record['title'])
    abstract = normalized(record.get('abstract', ''))
    matches, score = {}, 0
    for name, group in profile['groups'].items():
        in_title = [term for term in group['terms'] if contains(title, term)]
        in_abstract = [term for term in group['terms'] if contains(abstract, term)]
        terms = sorted(set(in_title + in_abstract))
        if terms:
            matches[name] = terms
            # Contar grupos, não frequência: repetição de palavras não infla a nota.
            score += group['weight'] * (3 if in_title else 1)
    eligible = any(all(group in matches for group in combination)
                   for combination in profile['required_any'])
    reasons = [profile['groups'][name]['label'] + ': ' + ', '.join(terms)
               for name, terms in matches.items()]
    return (score if eligible else 0), reasons


def identity_keys(record):
    keys = aliases(record)
    # Um artigo com DOI continua identificável por título/autor se a outra fonte omite DOI.
    if record.get('authors'):
        author = ' '.join(sorted(re.findall(r'\w+', normalized(record['authors'][0]))))
        title = re.sub(r'\W+', '', normalized(record['title']))
        keys.add('title-author:' + title + ':' + author)
    return keys


def deduplicate(records):
    """Agrupa identidades antes de limitar o número de artigos."""
    groups, lookup = {}, {}
    for original in records:
        record = deepcopy(original)
        record['doi'] = doi(record.get('doi'))
        keys = identity_keys(record)
        found = {lookup[key] for key in keys if key in lookup}
        if not found:
            group_id = max(groups, default=-1) + 1
            groups[group_id] = record
        else:
            group_id = min(found)
            for other in sorted(found - {group_id}):
                merge(groups[group_id], groups.pop(other))
                for key, value in list(lookup.items()):
                    if value == other:
                        lookup[key] = group_id
            merge(groups[group_id], record)
        for key in keys | identity_keys(groups[group_id]):
            lookup[key] = group_id
    return list(groups.values())


def merge(old, new):
    for field in ('category', 'source', 'source_ids'):
        old[field] = sorted(set(old.get(field, [])) | set(new.get(field, [])))
    if not old.get('authors'):
        old['authors'] = new.get('authors', [])
    if not old.get('doi'):
        old['doi'] = new.get('doi')
    if old.get('type') == 'unknown' and new['type'] != 'unknown':
        for field in ('type', 'date', 'url'):
            old[field] = new[field]
        old.pop('date_basis', None)
    if not old.get('abstract') or (old.get('abstract_basis') == 'feed_summary' and
                                  new.get('abstract') and not new.get('abstract_basis')):
        old['abstract'] = new.get('abstract', '')
        old.pop('abstract_basis', None)
        if new.get('abstract_basis'):
            old['abstract_basis'] = new['abstract_basis']
    old['cited_by_count'] = max(old.get('cited_by_count', 0), new.get('cited_by_count', 0))


def collect_candidates(client, config, profile):
    """Amostras por relevância; não tenta indexar todo o catálogo das fontes."""
    records, reports = [], []
    settings = config['candidate_search']
    per_query = int(settings.get('openalex_per_query', 100))
    if not 1 <= per_query <= 200:
        raise ValueError('openalex_per_query deve estar entre 1 e 200')
    key = os.environ.get('OPENALEX_API_KEY')
    if key:
        for query in profile['openalex_queries']:
            print(f'OpenAlex: candidatos por relevância para {query}', flush=True)
            try:
                # A ausência de from/to_publication_date permite artigos de qualquer ano.
                data = client.get('https://api.openalex.org/works', dict(
                    search=query, filter='type:article', per_page=per_query,
                    cursor='*', api_key=key)).json()
                batch = [openalex_record(w, profile['name']) for w in data['results']]
                for record, work in zip(batch, data['results']):
                    record['cited_by_count'] = work.get('cited_by_count', 0)
                records.extend(batch)
                reports.append(dict(source='OpenAlex', query=query, status='ok', candidates=len(batch)))
            except (RuntimeError, requests.RequestException, ValueError, KeyError, ET.ParseError):
                reports.append(dict(source='OpenAlex', query=query, status='unavailable'))
                print('Consulta OpenAlex indisponível; avaliando as demais fontes.', flush=True)
    else:
        reports.append(dict(source='OpenAlex', status='missing_api_key'))
    if settings.get('arxiv', True):
        try:
            response = client.get('https://export.arxiv.org/api/query', dict(
                search_query=profile['arxiv_query'], start=0,
                max_results=int(settings.get('arxiv_limit', 100)), sortBy='relevance'))
            batch, _ = arxiv_records(response.content, profile['name'])
            records.extend(batch)
            reports.append(dict(source='arXiv', status='ok', candidates=len(batch)))
        except (RuntimeError, requests.RequestException, ValueError, KeyError, ET.ParseError):
            reports.append(dict(source='arXiv', status='unavailable'))
    if settings.get('philpapers', True):
        for source in config.get('philpapers', []):
            try:
                url = source.get('feed_url') or discover_philpapers_feed(client, source['page_url'])
                response = download_philpapers_feed(client, url)
                # Datas dos alertas não restringem a inclusão de candidatos históricos.
                batch = philpapers_records(response.content, source['category'], None, None)
                records.extend(batch)
                reports.append(dict(source='PhilPapers', category=source['category'],
                                    status='ok', candidates=len(batch)))
            except (RuntimeError, requests.RequestException, ValueError, KeyError, ET.ParseError):
                reports.append(dict(source='PhilPapers', category=source['category'], status='unavailable'))
    return records, reports


def week_start(day):
    return day - timedelta(days=day.weekday())


def history_keys(root):
    seen = set()
    ledger = root / 'data/selection_state.json'
    if ledger.exists():
        seen.update(json.loads(ledger.read_text())['used_aliases'])
    for path in (root / 'docs/publications').glob('*.md'):
        seen.update(identity_keys(read_note(path)))
    return seen


def select(records, profile, used, limit):
    candidates = []
    for record in deduplicate(records):
        if record['type'] not in profile['allowed_types']:
            continue
        if identity_keys(record) & used:
            continue
        score, reasons = relevance(record, profile)
        if score < profile['minimum_score']:
            continue
        record['selection_score'] = score
        record['selection_reasons'] = reasons
        text = normalized(record['title'] + ' ' + record.get('abstract', ''))
        groups = {name for name, group in profile['groups'].items()
                  if any(contains(text, term) for term in group['terms'])}
        record['selection_questions'] = [axis['question'] for axis in profile.get('research_axes', [])
                                         if all(group in groups for group in axis['groups'])]
        record['selection_basis'] = 'Regras lexicais sobre título e resumo; avaliação bibliográfica automática.'
        candidates.append(record)
    # Data de publicação não participa do ranking. Citações só desempatarão a relevância.
    candidates.sort(key=lambda r: (-r['selection_score'], -r.get('cited_by_count', 0),
                                   normalized(r['title']), r.get('doi') or r['url']))
    # Reservar primeiro uma contribuição elegível para cada pergunta, quando houver.
    chosen = []
    remaining = list(candidates)
    for axis in profile.get('research_axes', []):
        if len(chosen) == limit:
            break
        match = next((r for r in remaining if axis['question'] in r['selection_questions']), None)
        if match is not None:
            chosen.append(match)
            remaining.remove(match)
    chosen.extend(remaining[:limit - len(chosen)])
    return chosen


def publish_week(root, day, records, profile, reports=None):
    limit = profile['articles_per_week']
    if type(limit) is not int or not 1 <= limit <= 10:
        raise ValueError('articles_per_week deve estar entre 1 e 10')
    monday = week_start(day)
    manifest = root / f'data/editions/{monday}.json'
    # Inclui qualquer edição da mesma semana, mesmo se alguém mudou o nome do arquivo.
    for path in (root / 'data/editions').glob('*.json'):
        old = json.loads(path.read_text())
        if week_start(date.fromisoformat(old['date'])) == monday:
            if len(old['ids']) > limit:
                raise RuntimeError('Edição existente excede o limite; revise antes de publicar.')
            print(f'A semana {monday} já tem uma edição. Nenhum artigo foi acrescentado.')
            return old
    used = history_keys(root)
    chosen = select(records, profile, used, limit)
    if len(chosen) < limit:
        raise RuntimeError(f'Só há {len(chosen)} candidatos inéditos com relevância suficiente; '
                           f'são necessários {limit}. Nenhuma edição foi gravada. '
                           'Amplie as consultas do perfil ou revise seus critérios.')
    for record in chosen:
        record['selected_at'] = day.isoformat()
        record['selection_week'] = monday.isoformat()
    ids = save_records(chosen, root)
    if len(ids) != limit:
        raise RuntimeError('A deduplicação final não produziu o total esperado; não publique esta execução.')
    edition = dict(date=monday.isoformat(), week_start=monday.isoformat(),
                   week_end_exclusive=(monday + timedelta(days=7)).isoformat(),
                   selected_at=day.isoformat(), selection_mode='research_relevance',
                   research_focus=profile['name'], ids=ids, candidate_count=len(records),
                   sources=reports or [])
    write(manifest, json.dumps(edition, ensure_ascii=False, indent=2) + '\n')
    for record in chosen:
        used.update(identity_keys(record))
    write(root / 'data/selection_state.json', json.dumps(
        dict(version=1, used_aliases=sorted(used)), ensure_ascii=False, indent=2) + '\n')
    return edition


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--date', type=date.fromisoformat,
                        default=datetime.now(ZoneInfo('America/Fortaleza')).date(),
                        help='Data editorial local; não filtra a data dos artigos.')
    args = parser.parse_args()
    profile = yaml.safe_load((ROOT / 'research_profile.yml').read_text())
    config = yaml.safe_load((ROOT / 'topics.yml').read_text())
    # Uma reexecução da mesma semana dispensa até as consultas de rede.
    for path in (ROOT / 'data/editions').glob('*.json'):
        edition = json.loads(path.read_text())
        if week_start(date.fromisoformat(edition['date'])) == week_start(args.date):
            print(f'Edição de {week_start(args.date)} já publicada; preservando os artigos.')
            return
    contact = os.environ.get('CONTACT_EMAIL', '')
    if '@' not in contact:
        raise SystemExit('Configure CONTACT_EMAIL com um contato válido para as fontes.')
    try:
        records, reports = collect_candidates(Client(contact), config, profile)
        edition = publish_week(ROOT, args.date, records, profile, reports)
    except (RuntimeError, ValueError) as exc:
        raise SystemExit(str(exc)) from None
    print(f'Edição {edition["date"]}: {len(edition["ids"])} artigos selecionados por relevância.')


if __name__ == '__main__':
    main()
