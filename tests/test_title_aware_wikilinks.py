import importlib.util
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / 'hooks' / 'title_aware_wikilinks.py'
spec = importlib.util.spec_from_file_location('title_aware_wikilinks', MODULE_PATH)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)


class TitleAwareWikiLinksTests(unittest.TestCase):
    def test_extract_page_title_prefers_frontmatter_title(self):
        text = """---
title: Custom Title
type: summary
---

# Heading Title
"""
        self.assertEqual(module.extract_page_title(text), 'Custom Title')

    def test_rewrite_bare_wikilink_uses_target_page_title(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            docs_dir = Path(tmpdir)
            (docs_dir / 'swift-language-overview.md').write_text(
                """---
type: summary
---

# Swift 언어 개요
""",
                encoding='utf-8',
            )

            module.build_title_maps(docs_dir)
            rewritten = module.rewrite_bare_wikilinks('go to [[swift-language-overview]]')
            self.assertEqual(
                rewritten,
                'go to [[swift-language-overview|Swift 언어 개요]]',
            )

    def test_rewrite_preserves_explicit_alias(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            docs_dir = Path(tmpdir)
            (docs_dir / 'swift-language-overview.md').write_text('# Swift 언어 개요\n', encoding='utf-8')

            module.build_title_maps(docs_dir)
            rewritten = module.rewrite_bare_wikilinks(
                'go to [[swift-language-overview|Custom Label]]'
            )
            self.assertEqual(rewritten, 'go to [[swift-language-overview|Custom Label]]')

    def test_rewrite_anchor_uses_page_title_plus_anchor(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            docs_dir = Path(tmpdir)
            (docs_dir / 'swift-language-overview.md').write_text('# Swift 언어 개요\n', encoding='utf-8')

            module.build_title_maps(docs_dir)
            rewritten = module.rewrite_bare_wikilinks(
                'go to [[swift-language-overview#추천 읽기 순서]]'
            )
            self.assertEqual(
                rewritten,
                'go to [[swift-language-overview#추천 읽기 순서|Swift 언어 개요#추천 읽기 순서]]',
            )


if __name__ == '__main__':
    unittest.main()
