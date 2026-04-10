import importlib.util
import tempfile
import time
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / 'scripts' / 'wikictl.py'
spec = importlib.util.spec_from_file_location('wikictl', MODULE_PATH)
wikictl = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(wikictl)


class WikiCtlTests(unittest.TestCase):
    def test_extract_nav_page_paths_reads_nested_mkdocs_nav(self):
        text = '''
site_name: Demo
nav:
  - Home: index.md
  - 개요:
    - overview.md
    - compiling-swift-generics.md
  - SIL:
    - sil-reference.md
'''
        self.assertEqual(
            wikictl.extract_nav_page_paths(text),
            ['index.md', 'overview.md', 'compiling-swift-generics.md', 'sil-reference.md'],
        )

    def test_find_unlisted_pages_returns_pages_missing_from_nav(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            (root / 'pages').mkdir()
            (root / 'site').mkdir()
            (root / 'mkdocs.yml').write_text('''\
site_name: Demo
nav:
  - Home: index.md
  - overview.md
''')
            for name in ['index.md', 'overview.md', 'new-page.md']:
                (root / 'pages' / name).write_text(f'# {name}\n')

            self.assertEqual(wikictl.find_unlisted_pages(root), ['new-page.md'])

    def test_site_is_stale_when_pages_are_newer_than_built_site(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            (root / 'pages').mkdir()
            (root / 'site').mkdir()
            (root / 'mkdocs.yml').write_text('site_name: Demo\nnav:\n  - index.md\n')
            page = root / 'pages' / 'index.md'
            page.write_text('# page\n')
            site_index = root / 'site' / 'index.html'
            site_index.write_text('<html></html>\n')

            old = time.time() - 10
            new = time.time()
            import os
            os.utime(site_index, (old, old))
            os.utime(page, (new, new))
            os.utime(root / 'mkdocs.yml', (old, old))

            self.assertTrue(wikictl.site_is_stale(root))


if __name__ == '__main__':
    unittest.main()
