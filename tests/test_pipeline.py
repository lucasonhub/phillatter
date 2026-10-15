import json
from pathlib import Path
import sys
import tempfile
import unittest
from datetime import date, timedelta
from unittest.mock import patch
import xml.etree.ElementTree as ET
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from collect import arxiv_records, collect, collect_openalex, inverted_abstract, read_note, save_records
from render_site import render


class Response:
    def __init__(self, data):
        self.data = data
    def json(self):
        return self.data


class PipelineTest(unittest.TestCase):
    def record(self, **kw):
        return dict(title='Mente --- <script>alert(1)</script>', authors=['Ana'], date='2026-10-14',
                    type='article', category=['Neurociência'], doi='10.1234/test', abstract='Um [link](https://test).',
                    source=['OpenAlex'], source_ids=['https://openalex.org/W1'], url='https://doi.org/10.1234/test') | kw

    def test_abstract(self):
        self.assertEqual(inverted_abstract({'world': [1], 'Hello': [0, 2]}), 'Hello world Hello')
        self.assertEqual(inverted_abstract(None), '')

    def test_arxiv(self):
        xml = '''<feed xmlns="http://www.w3.org/2005/Atom" xmlns:o="http://a9.com/-/spec/opensearch/1.1/" xmlns:x="http://arxiv.org/schemas/atom"><o:totalResults>1</o:totalResults><entry><id>http://arxiv.org/abs/2610.12345v2</id><title>Some\n work</title><published>2026-10-14T10:00:00Z</published><author><name>Ana</name></author><summary>Abstract</summary><x:doi>https://doi.org/10.1234/Test</x:doi></entry></feed>'''
        records, total = arxiv_records(xml, 'IA')
        self.assertEqual(total, 1)
        self.assertEqual(records[0]['doi'], '10.1234/test')
        self.assertEqual(records[0]['source_ids'], ['arxiv:2610.12345'])
        self.assertEqual(records[0]['type'], 'preprint')

    def test_pagination_and_window(self):
        calls = []
        class Client:
            content = b''
            def get(self, url, params):
                if 'arxiv' in url:
                    return self
                calls.append(params)
                return Response({'meta': {'count': 1, 'next_cursor': 'next' if params['cursor'] == '*' else None},
                                 'results': [{'id': 'W1', 'title': 'Mind', 'type': 'article', 'publication_date': '2026-10-14'}] if params['cursor'] == '*' else []})
        config = {'categories': {'IA': {'openalex': ['mind'], 'arxiv': 'cat:cs.AI'}}}
        with patch.dict('os.environ', {'OPENALEX_API_KEY': 'test'}), patch('collect.arxiv_records', return_value=([], 0)):
            rows = collect(Client(), config, date(2026, 10, 8), date(2026, 10, 15))
        self.assertEqual(len(rows), 1)
        self.assertIn('from_publication_date:2026-10-08,to_publication_date:2026-10-14', calls[0]['filter'])
        self.assertEqual(calls[1]['cursor'], 'next')

    def test_limits_fail(self):
        class Client:
            def get(self, url, params):
                return Response({'meta': {'count': 99999}, 'results': []})
        with patch.dict('os.environ', {'OPENALEX_API_KEY': 'test'}):
            with self.assertRaises(RuntimeError):
                collect(Client(), {'categories': {'IA': {'openalex': ['a'], 'arxiv': 'a'}}}, date(2026, 10, 8), date(2026, 10, 15))

    def test_openalex_splits_without_gaps_or_duplicates(self):
        accepted_windows = []
        class Client:
            def get(self, url, params):
                pieces = dict(p.split(':', 1) for p in params['filter'].split(','))
                first = date.fromisoformat(pieces['from_publication_date'])
                last = date.fromisoformat(pieces['to_publication_date'])
                days = (last - first).days + 1
                if days <= 2:
                    accepted_windows.append((first, last))
                rows = [dict(id=f'W{first + timedelta(days=i)}', title='Mind', type='article',
                             publication_date=str(first + timedelta(days=i))) for i in range(days)]
                return Response({'meta': {'count': days, 'next_cursor': None}, 'results': rows})
        start, end = date(2026, 10, 8), date(2026, 10, 15)
        rows = collect_openalex(Client(), 'mind', 'Mente', start, end, 'test', 2)
        expected = [str(start + timedelta(days=i)) for i in range(7)]
        self.assertEqual([r['date'] for r in rows], expected)
        self.assertEqual(len({r['source_ids'][0] for r in rows}), 7)
        self.assertTrue(all((b - a).days < 2 for a, b in accepted_windows))

    def test_openalex_single_day_limit_is_explicit(self):
        class Client:
            def get(self, url, params):
                return Response({'meta': {'count': 6000}, 'results': []})
        with self.assertRaisesRegex(RuntimeError, 'no dia 2026-10-08'):
            collect_openalex(Client(), 'mind', 'Mente', date(2026, 10, 8), date(2026, 10, 9), 'test', 5000)

    def test_dedup_markdown_and_rss(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            second = self.record(source=['arXiv'], source_ids=['arxiv:2610.12345'], category=['IA'], type='preprint')
            ids = save_records([self.record(), second], root)
            self.assertEqual(len(ids), 1)
            self.assertEqual(save_records([second], root), [])
            path = root / f'docs/publications/{ids[0]}.md'
            self.assertEqual(read_note(path)['category'], ['IA', 'Neurociência'])
            # O frontmatter preserva texto original; só o corpo escapa conteúdo.
            self.assertNotIn('<script>', path.read_text().split('\n---\n', 1)[1])
            self.assertIn('\\[link\\]', path.read_text())
            d = root / 'data/editions'
            d.mkdir(parents=True)
            (d / '2026-10-15.json').write_text(json.dumps(dict(date='2026-10-15', start='2026-10-08', end_exclusive='2026-10-15', ids=ids)))
            render(root, 'https://example.org/repo/')
            rss = ET.fromstring((root / 'docs/feed.xml').read_text())
            self.assertEqual(rss.findtext('channel/item/link'), 'https://example.org/repo/editions/2026-10-15/')
            self.assertIn('&lt;script&gt;', (root / 'docs/index.md').read_text())
            first = (root / 'docs/feed.xml').read_text()
            render(root, 'https://example.org/repo/')
            self.assertEqual(first, (root / 'docs/feed.xml').read_text())


if __name__ == '__main__':
    unittest.main()
