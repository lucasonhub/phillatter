from copy import deepcopy
from datetime import date
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
import yaml
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from curate import (collect_candidates, deduplicate, history_keys, publish_week,
                    relevance, select, week_start)
from render_site import render

PROFILE = yaml.safe_load((Path(__file__).resolve().parents[1] / 'research_profile.yml').read_text())


def article(number, **changes):
    return dict(title=f'Computational theory of mind and intentionality: argument {number}',
                authors=[f'Author {number}'], date='1975-01-01', type='article',
                category=['Teoria computacional da mente'], doi=f'10.1234/paper{number}',
                abstract='Mental content and symbolic representation in computationalism.',
                source=['OpenAlex'], source_ids=[f'W{number}'], url=f'https://doi.org/10.1234/paper{number}') | changes


class CurationTest(unittest.TestCase):
    def test_research_focus_excludes_generic_ai(self):
        good, _ = relevance(article(1), PROFILE)
        bad, _ = relevance(article(2, title='Machine learning for stock prices', abstract='A new accuracy benchmark.'), PROFILE)
        self.assertGreater(good, bad)
        self.assertEqual(bad, 0)

    def test_old_relevant_article_is_eligible(self):
        rows = select([article(1, date='1950-01-01'), article(2, title='Recent database benchmark', abstract='Results', date='2026-10-28')], PROFILE, set(), 10)
        self.assertEqual([r['doi'] for r in rows], ['10.1234/paper1'])
        self.assertTrue(rows[0]['selection_reasons'])

    def test_books_and_unverified_types_are_excluded(self):
        rows = select([article(1, type='book'), article(2, type='unknown'), article(3, type='article')], PROFILE, set(), 10)
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]['type'], 'article')

    def test_duplicates_do_not_consume_slots(self):
        a = article(1)
        b = article(1, doi='https://doi.org/10.1234/PAPER1', source=['arXiv'], source_ids=['arxiv:1'])
        rows = deduplicate([a, b])
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]['source'], ['OpenAlex', 'arXiv'])

    def test_profile_covers_research_questions_before_repeating_one_axis(self):
        records = [article(i) for i in range(15)]
        foundational = article(999, title='What is computation? Physical computation and its boundaries',
                               abstract='A study of physical computation.', doi='10.1234/foundational')
        rows = select(records + [foundational], PROFILE, set(), 10)
        self.assertEqual(len(rows), 10)
        self.assertIn('10.1234/foundational', [r['doi'] for r in rows])
        self.assertTrue(any(PROFILE['research_questions'][0] in r['selection_questions'] for r in rows))

    def test_week_is_monday_to_sunday(self):
        self.assertEqual(week_start(date(2026, 10, 28)), date(2026, 10, 26))
        self.assertEqual(week_start(date(2026, 11, 1)), date(2026, 10, 26))

    def test_ten_per_week_and_same_week_rerun(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            records = [article(i) for i in range(30)]
            first = publish_week(root, date(2026, 10, 28), records, PROFILE)
            self.assertEqual(len(first['ids']), 10)
            second = publish_week(root, date(2026, 10, 30), records, PROFILE)
            self.assertEqual(first, second)
            self.assertEqual(len(list((root / 'docs/publications').glob('*.md'))), 10)
            next_week = publish_week(root, date(2026, 11, 2), records, PROFILE)
            self.assertFalse(set(first['ids']) & set(next_week['ids']))
            self.assertEqual(len(list((root / 'docs/publications').glob('*.md'))), 20)
            self.assertTrue((root / 'data/selection_state.json').exists())

    def test_shortage_does_not_create_partial_edition(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            with self.assertRaisesRegex(RuntimeError, 'Só há 9'):
                publish_week(root, date(2026, 10, 28), [article(i) for i in range(9)], PROFILE)
            self.assertFalse(list(root.rglob('*.md')))
            self.assertFalse(list(root.rglob('*.json')))

    def test_limit_above_ten_is_rejected(self):
        profile = deepcopy(PROFILE)
        profile['articles_per_week'] = 11
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(ValueError):
                publish_week(Path(tmp), date(2026, 10, 28), [article(i) for i in range(20)], profile)

    def test_ledger_prevents_repeat_even_if_note_is_missing(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            edition = publish_week(root, date(2026, 10, 28), [article(i) for i in range(10)], PROFILE)
            for path in (root / 'docs/publications').glob('*.md'):
                path.unlink()
            self.assertEqual(select([article(i) for i in range(10)], PROFILE, history_keys(root), 10), [])

    def test_historical_openalex_has_no_date_filter(self):
        calls = []
        class Client:
            def get(self, url, params):
                calls.append(params)
                return type('R', (), {'json': lambda self: {'results': [dict(id='W1', title='Computationalism', type='article', publication_date='1950-01-01')]}})()
        profile = deepcopy(PROFILE)
        profile['openalex_queries'] = ['computationalism']
        config = dict(candidate_search=dict(openalex_per_query=100, arxiv=False, philpapers=False))
        with patch.dict('os.environ', {'OPENALEX_API_KEY': 'test'}):
            rows, reports = collect_candidates(Client(), config, profile)
        self.assertEqual(calls[0]['filter'], 'type:article')
        self.assertNotIn('from_publication_date', str(calls))
        self.assertEqual(rows[0]['date'], '1950-01-01')

    def test_render_prunes_old_feed_content_and_limits_rss(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for sub in ('docs/publications', 'docs/editions'):
                (root / sub).mkdir(parents=True)
            (root / 'docs/publications/old.md').write_text('OLD CONTENT')
            (root / 'docs/editions/2020-01-01.md').write_text('OLD CONTENT')
            render(root, 'https://example.org/repo/')
            self.assertFalse((root / 'docs/publications/old.md').exists())
            self.assertNotIn('OLD CONTENT', (root / 'docs/feed.xml').read_text())
            publish_week(root, date(2026, 10, 28), [article(i) for i in range(10)], PROFILE)
            render(root, 'https://example.org/repo/')
            self.assertIn('1975-01-01', (root / 'docs/index.md').read_text())
            self.assertEqual(len(list((root / 'docs/publications').glob('*.md'))), 10)
            self.assertIn('Semana editorial', (root / 'docs/editions/2026-10-26.md').read_text())


if __name__ == '__main__':
    unittest.main()
