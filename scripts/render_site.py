"""Índices e RSS derivados dos Markdown e manifests locais, sem rede."""
from collections import defaultdict
from datetime import datetime, timezone
from email.utils import format_datetime
import html
import json
from pathlib import Path
from urllib.parse import urlparse
import xml.etree.ElementTree as ET

from collect import ROOT, frontmatter, markdown, read_note, write


def render(root=ROOT, site_url='http://127.0.0.1:8000/'):
    site_url = site_url.rstrip('/') + '/'
    if urlparse(site_url).scheme not in ('https', 'http'):
        raise ValueError('SITE_URL precisa começar com https:// ou http://')
    docs = root / 'docs'
    editions = [json.loads(p.read_text()) for p in sorted((root / 'data/editions').glob('*.json'), reverse=True)]
    if any(len(e['ids']) > 10 for e in editions):
        raise ValueError('Uma edição excede o limite de dez artigos.')
    included = {uid for edition in editions for uid in edition['ids']}
    # Pastas geradas: nenhum arquivo fora das edições pode entrar no site/busca.
    for path in (docs / 'publications').glob('*.md'):
        if path.stem not in included:
            path.unlink()
    valid_editions = {edition['date'] for edition in editions}
    for path in (docs / 'editions').glob('*.md'):
        if path.name != 'index.md' and path.stem not in valid_editions:
            path.unlink()
    notes = {uid: read_note(docs / f'publications/{uid}.md') for uid in included}
    order = lambda x: (x[1].get('selection_week', x[1]['date']), x[1].get('selection_score', 0), x[0])
    by_category = defaultdict(list)
    for uid, note in sorted(notes.items(), key=order, reverse=True):
        for category in note['category']:
            by_category[category].append((uid, note))
    index = ['# Phillater', 'Dez artigos por semana sobre os fundamentos, alcance e limites da teoria computacional da mente, orientados pelas perguntas da dissertação.',
             '[Ler edições](editions/index.md) · [Explorar temas](categories.md) · [Assinar RSS](feed.xml)',
             'Use a busca no topo para pesquisar títulos, autores e resumos.',
             '## Artigos selecionados', '<label for="topic">Filtrar por tema</label>',
             '<select id="topic"><option value="">Todos os temas</option>']
    for category in sorted(by_category):
        index.append(f'<option>{html.escape(category)}</option>')
    index.extend(['</select>', '<p id="result-count" aria-live="polite"></p>', '<div class="papers">'])
    for uid, note in sorted(notes.items(), key=order, reverse=True):
        cats = html.escape(json.dumps(note['category'], ensure_ascii=False), quote=True)
        index.append(f'<article class="paper" data-topics="{cats}"><small>{html.escape(note["date"])} · '
                     f'{html.escape(note["type"])}</small><h3><a href="publications/{uid}/">'
                     f'{html.escape(note["title"])}</a></h3><p>{html.escape("; ".join(note["authors"]))}</p>'
                     f'<p>{html.escape((note["abstract"] or "Resumo indisponível.")[:350])}</p>'
                     f'<small>{html.escape(" · ".join(note["category"]))}</small></article>')
    index.append('</div>')
    if not notes:
        index.append('O acervo anterior foi reiniciado. A próxima edição trará dez artigos selecionados por relevância, de qualquer ano.')
    write(docs / 'index.md', '\n\n'.join(index) + '\n')
    categories = ['# Temas', 'Selecione um tema na página inicial ou navegue pelos títulos abaixo.']
    for category, entries in sorted(by_category.items()):
        categories.append('## ' + markdown(category))
        categories.extend(f'- [{markdown(n["title"])}](publications/{uid}.md)' for uid, n in entries)
    write(docs / 'categories.md', '\n\n'.join(categories) + '\n')
    archive = ['# Edições semanais']
    rss = ET.Element('rss', version='2.0')
    channel = ET.SubElement(rss, 'channel')
    for tag, text in [('title', 'Phillater'), ('link', site_url), ('language', 'pt-br'),
                      ('description', 'Curadoria acadêmica: teoria computacional da mente, representação simbólica e intencionalidade')]:
        ET.SubElement(channel, tag).text = text
    for edition in editions:
        day = edition['date']
        title = f'Phillater — {day}'
        archive.append(f'- [{title}]({day}.md) — {len(edition["ids"])} artigos selecionados')
        if edition.get('selection_mode') == 'research_relevance':
            scope = (f'Semana editorial: {edition["week_start"]} até {edition["week_end_exclusive"]} '
                     f'(fim exclusivo). Seleção em {edition["selected_at"]}.')
        else:
            scope = f'Janela UTC: {edition["start"]} até {edition["end_exclusive"]} (fim exclusivo).'
        body = [f'# {title}', scope,
                'A data dos artigos pode ser antiga. A seleção usa um perfil de pesquisa e regras explícitas sobre títulos e resumos; não substitui a leitura crítica. Resumos e descrições são preservados das fontes. Preprints são identificados como tal.']
        description = []
        for uid in edition['ids']:
            note = notes[uid]
            body.extend([f'## [{markdown(note["title"])}](../publications/{uid}.md)',
                         markdown('; '.join(note['authors'])),
                         f"**Publicação:** {note['date']} · **Tipo:** {note['type']}",
                         markdown(note['abstract'] or 'Resumo indisponível na fonte.')])
            if note.get('selection_reasons'):
                body.append('**Relação com a pesquisa:** ' + markdown('; '.join(note['selection_reasons'])))
            url = site_url + f'publications/{uid}/'
            description.append(f'<p><a href="{html.escape(url, quote=True)}">{html.escape(note["title"])}</a></p>'
                               f'<p>{html.escape(note["abstract"] or "Resumo indisponível.")}</p>')
        if not edition['ids']:
            body.append('Nenhuma publicação nova encontrada nesta execução.')
        write(docs / f'editions/{day}.md', frontmatter({'title': title, 'date': day}, '\n\n'.join(body)))
        if len(channel.findall('item')) < 52:
            item = ET.SubElement(channel, 'item')
            link = site_url + f'editions/{day}/'
            for tag, value in [('title', title), ('link', link), ('guid', link),
                               ('pubDate', format_datetime(datetime.fromisoformat(day).replace(tzinfo=timezone.utc))),
                               ('description', ''.join(description) or 'Nenhuma publicação nova.')]:
                ET.SubElement(item, tag).text = value
    write(docs / 'editions/index.md', '\n\n'.join(archive) + '\n')
    write(docs / 'feed.xml', ET.tostring(rss, encoding='unicode', xml_declaration=True))


if __name__ == '__main__':
    import os
    render(site_url=os.environ.get('SITE_URL', 'http://127.0.0.1:8000/'))
