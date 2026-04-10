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

    def test_build_status_snapshot_counts_nested_pages(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            (root / 'pages' / 'downloads').mkdir(parents=True)
            (root / 'sources').mkdir()
            (root / 'site').mkdir()
            (root / 'mkdocs.yml').write_text('''\
site_name: Demo
site_url: https://example.com/
nav:
  - Home: index.md
  - Downloads: downloads/index.md
''')
            (root / 'pages' / 'index.md').write_text('# home\n')
            (root / 'pages' / 'downloads' / 'index.md').write_text('# downloads\n')
            (root / 'site' / 'index.html').write_text('<html></html>\n')
            (root / 'site' / 'downloads').mkdir()
            (root / 'site' / 'downloads' / 'index.html').write_text('<html></html>\n')

            import subprocess
            subprocess.check_call(['git', 'init'], cwd=root)
            subprocess.check_call(['git', 'config', 'user.email', 'test@example.com'], cwd=root)
            subprocess.check_call(['git', 'config', 'user.name', 'Test User'], cwd=root)
            subprocess.check_call(['git', 'add', '.'], cwd=root)
            subprocess.check_call(['git', 'commit', '-m', 'init'], cwd=root)

            snapshot = wikictl.build_status_snapshot(root)
            self.assertEqual(snapshot['pages'], 2)

    def test_stage_static_files_copies_files_tree_into_site(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            (root / 'files' / 'downloads').mkdir(parents=True)
            (root / 'site').mkdir()
            (root / 'files' / 'downloads' / 'bundle.zip').write_bytes(b'zip')
            (root / 'files' / 'downloads' / 'doc.md').write_text('# raw\n')

            wikictl.stage_static_files(root)

            self.assertTrue((root / 'site' / 'files' / 'downloads' / 'bundle.zip').exists())
            self.assertTrue((root / 'site' / 'files' / 'downloads' / 'doc.md').exists())

    def test_sanitize_download_bundle_metadata_rewrites_absolute_paths_as_relative(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            bundle_dir = Path(tmpdir) / 'files' / 'downloads' / 'swift-docs-test'
            bundle_dir.mkdir(parents=True)
            manifest = bundle_dir / 'MANIFEST.json'
            manifest.write_text('''{
  "base_dir": "/Users/test/Downloads/swift-docs-test",
  "downloaded": [
    {
      "save_as": "swiftlang-swift/docs/TypeChecker.md",
      "saved_path": "/Users/test/Downloads/swift-docs-test/files/swiftlang-swift/docs/TypeChecker.md"
    }
  ]
}
''')
            readme = bundle_dir / 'README.txt'
            readme.write_text('Swift docs local bundle\nBase: /Users/test/Downloads/swift-docs-test\n')

            wikictl.sanitize_download_bundle_metadata(bundle_dir)

            self.assertIn('"base_dir": "."', manifest.read_text())
            self.assertIn('"saved_path": "files/swiftlang-swift/docs/TypeChecker.md"', manifest.read_text())
            self.assertEqual(readme.read_text(), 'Swift docs local bundle\nBase: .\n')

    def test_find_sensitive_local_path_hits_detects_public_local_paths(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            (root / 'pages').mkdir()
            (root / 'sources').mkdir()
            (root / 'files' / 'downloads' / 'bundle').mkdir(parents=True)
            (root / 'site').mkdir()
            (root / 'mkdocs.yml').write_text('site_name: Demo\nnav:\n  - Home: index.md\n')
            (root / 'pages' / 'index.md').write_text('open /Users/test/swift/README.md\n')
            (root / 'files' / 'downloads' / 'bundle' / 'README.txt').write_text('Base: /Users/test/Downloads/swift-docs-test\n')

            hits = wikictl.find_sensitive_local_path_hits(root)

            self.assertTrue(any(hit['path'].endswith('pages/index.md') for hit in hits))
            self.assertTrue(any(hit['path'].endswith('files/downloads/bundle/README.txt') for hit in hits))


if __name__ == '__main__':
    unittest.main()
