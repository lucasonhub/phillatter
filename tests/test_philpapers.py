from datetime import date
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from collect import (collect, collect_philpapers, discover_philpapers_feed,
                     philpapers_records, read_note, save_records)

START, END = date(2026, 10, 8), date(2026, 10, 15)


def feed(items):
    return f'''<?xml version="1.0"?><rss version="2.0" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:prism="http://prismstandard.org/namespaces/basic/2.0/"><channel><title>PhilPapers</title><link>https://philpapers.org/</link><description>New items</description>{items}</channel></rss>'''.encode()


def item(stamp='Wed, 14 Oct 2026 12:00:00 GMT', identifier='TEST', extra=''):
    published = f'<pubDate>{stamp}</pubDate>' if stamp else ''
    return f'''<item><title>Mind &amp; Cognition</title><link>https://philpapers.org/rec/{identifier}?source=rss</link><guid>https://philpapers.org/rec/{identifier}</guid>{published}<dc:creator>Ana Silva</dc:creator><description>&lt;p&gt;Feed description.&lt;/p&gt;</description>{extra}</item>'''


class PhilPapersTest(unittest.TestCase):
    def test_window_and_fields(self):
        content = feed(item('Thu, 08 Oct 2026 00:00:00 GMT', 'FIRST') + item() +
                       item('Thu, 15 Oct 2026 00:00:00 GMT', 'NEXT') +
                       item('Wed, 07 Oct 2026 23:59:59 GMT', 'OLD'))
        rows = philpapers_records(content, 'Filosofia da Mente', START, END)
        self.assertEqual(len(rows), 2)
        row = rows[1]
        self.assertEqual(row['authors'], ['Ana Silva'])
        self.assertEqual(row['abstract'], 'Feed description.')
        self.assertEqual(row['type'], 'unknown')
        self.assertEqual(row['date_basis'], 'feed_published')
        self.assertEqual(row['url'], 'https://philpapers.org/rec/TEST')
        self.assertEqual(row['source'], ['PhilPapers'])

    def test_undated_and_updated(self):
        rows = philpapers_records(feed(item(None)), 'Mente', START, END, observed_on=END)
        self.assertEqual(rows[0]['date'], '2026-10-15')
        self.assertEqual(rows[0]['date_basis'], 'discovered')
        atom = b'''<feed xmlns="http://www.w3.org/2005/Atom"><title>PhilPapers</title><id>test</id><updated>2026-10-14T12:00:00Z</updated><entry><id>test</id><title>Mind</title><link href="https://philpapers.org/rec/TEST"/><updated>2026-10-14T12:00:00Z</updated></entry></feed>'''
        row = philpapers_records(atom, 'Mente', START, END)[0]
        self.assertEqual(row['date_basis'], 'feed_updated')
        self.assertEqual(row['authors'], [])
        self.assertEqual(row['abstract'], '')

    def test_malformed_and_nonfeed(self):
        for content in (b'<html><body>Access denied</body></html>', b'<rss><broken>'):
            with self.assertRaises(RuntimeError):
                philpapers_records(content, 'Mente', START, END)

    def test_discovery_and_explicit_url(self):
        class Client:
            calls = []
            def get(self, url, params):
                self.calls.append(url)
                self.text = '<html><link rel="alternate" type="application/rss+xml" href="/rss.pl?catId=123"/></html>'
                self.content = feed(item())
                return self
        client = Client()
        url = discover_philpapers_feed(client, 'https://philpapers.org/browse/philosophy-of-mind')
        self.assertEqual(url, 'https://philpapers.org/rss.pl?catId=123')
        rows = collect_philpapers(client, {'philpapers': [{'category': 'Mente', 'feed_url': url}]}, START, END)
        self.assertEqual(rows[0]['category'], ['Mente'])
        self.assertEqual(len(client.calls), 2)  # a URL explícita dispensa outra descoberta
        client.text = ''
        with self.assertRaises(RuntimeError):
            class NoRSS:
                def get(self, *args):
                    return type('R', (), {'text': '<html>No RSS</html>'})()
            discover_philpapers_feed(NoRSS(), 'https://philpapers.org/browse/philosophy-of-mind')

    def test_collection_integration_and_dedup(self):
        class Client:
            def get(self, url, params):
                return type('R', (), {'content': feed(item(extra='<prism:doi>10.1234/Test</prism:doi>'))})()
        config = {'categories': {}, 'philpapers': [
            {'category': 'Filosofia da Mente', 'feed_url': 'https://philpapers.org/rss.pl?catId=123'},
            {'category': 'Filosofia da Ciência Cognitiva', 'feed_url': 'https://philpapers.org/rss.pl?catId=456'}]}
        with patch.dict('os.environ', {'OPENALEX_API_KEY': 'test'}):
            rows = collect(Client(), config, START, END)
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0]['doi'], '10.1234/test')
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            ids = save_records(rows, root)
            self.assertEqual(len(ids), 1)
            self.assertEqual(save_records(rows, root), [])
            note = read_note(root / f'docs/publications/{ids[0]}.md')
            self.assertEqual(len(note['category']), 2)
            other = dict(note, source=['OpenAlex'], source_ids=['https://openalex.org/W1'],
                         type='article', abstract='Abstract original')
            other.pop('date_basis', None)
            other.pop('abstract_basis', None)
            self.assertEqual(save_records([other], root), [])
            note = read_note(root / f'docs/publications/{ids[0]}.md')
            self.assertEqual(note['source'], ['OpenAlex', 'PhilPapers'])
            self.assertEqual(note['type'], 'article')
            self.assertEqual(note['abstract'], 'Abstract original')
            self.assertNotIn('abstract_basis', note)


if __name__ == '__main__':
    unittest.main()
