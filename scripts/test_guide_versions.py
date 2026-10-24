"""Release boundaries and reading-site behavior contracts, without a product parser."""
import copy
import html
import json
import shutil
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import build_site as site
from capture_guide_release import capture


class GuideVersions(unittest.TestCase):
    def test_archive_label_and_current_stable_navigation_are_consistent(self):
        metadata = copy.deepcopy(site.VERSIONS)
        archived = next(r for r in metadata['versions'] if r['status'] == 'archive')
        archived['label'] = 'Actual product draft & corrected <name>'
        stable = next(r for r in metadata['versions'] if r['status'] == 'stable')
        with patch.object(site, 'VERSIONS', metadata):
            context = site.SiteContext(archived['version'], 'archive', site.PAGES, '../../', {})
            rendered = site.page_template('index', 'Guide', '<h1>Guide</h1>', [], None, None, context)
            menu = context.version_menu('index')
        self.assertIn(html.escape(archived['label']) + ' — 보존된 당시 안내입니다.', rendered)
        self.assertIn(f'<a href="../../index.html">{stable["label"]}</a>', menu)
        self.assertNotIn(f'<a href="../../versions/{stable["version"]}/index.html">', menu)

    def test_history_article_links_use_the_global_history_in_every_version(self):
        for version, status, prefix in [('0.3.37', 'stable', ''), ('0.3.39', 'preview', '../../')]:
            context = site.SiteContext(version, status, site.PAGES, prefix, {})
            self.assertEqual(site.rewrite_link('history.md', context), prefix + 'history.html')
            self.assertEqual(site.rewrite_link('history.md#versions', context), prefix + 'history.html#versions')

    def test_version_menu_does_not_link_an_unrendered_snapshot_page(self):
        context = site.SiteContext(site.APP_VERSION, 'stable', site.PAGES, '', {})
        menu = context.version_menu('history')
        self.assertIn('versions/0.3.37/index.html', menu)
        self.assertNotIn('versions/0.3.37/history.html', menu)

    def test_history_is_intact_and_cannot_be_recaptured(self):
        site.verify_history()
        with self.assertRaisesRegex(ValueError, 'already preserved'):
            capture('0.3.31', 'HEAD')

    def test_unannounced_promotion_is_rejected(self):
        metadata = copy.deepcopy(site.VERSIONS)
        metadata['authoringVersion'] = '9.9.9'
        with patch.object(site, 'VERSIONS', metadata), self.assertRaisesRegex(ValueError, 'promote explicitly'):
            site.verify_history()

    def test_preserved_source_tampering_is_rejected(self):
        scratch = site.ROOT / '.runtime'
        scratch.mkdir(exist_ok=True)
        for version in ('0.3.32', *site.CURRENT_GUIDE_ALIASES):
            with self.subTest(version=version), tempfile.TemporaryDirectory(dir=scratch) as directory:
                history = Path(directory)
                shutil.copytree(site.HISTORY, history, dirs_exist_ok=True)
                target = history / version / 'source/sharing.md'
                target.write_text('changed', encoding='utf-8')
                with patch.object(site, 'HISTORY', history), self.assertRaisesRegex(ValueError, 'preserved version changed'):
                    site.verify_history()

    def test_retired_drafts_are_not_in_public_catalog_or_search(self):
        for version in site.CURRENT_GUIDE_ALIASES:
            self.assertNotIn(version, [r['version'] for r in site.VERSIONS['versions']])
            for page in site.DOCS.rglob('*.html'):
                self.assertNotIn(version, page.read_text(encoding='utf-8'), str(page))
            for search in site.DOCS.rglob('search-index.js'):
                self.assertNotIn(version, search.read_text(encoding='utf-8'), str(search))
            self.assertTrue((site.HISTORY / version / 'integrity.json').is_file())

    def test_current_aliases_reconcile_old_payload_and_are_repeatable(self):
        with tempfile.TemporaryDirectory() as directory:
            docs = Path(directory) / 'docs'
            for version in site.CURRENT_GUIDE_ALIASES:
                old = docs / 'versions' / version
                for name in ('source/index.md', 'examples/old.json', 'assets/search-index.js', 'unknown.html'):
                    target = old / name
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_text('old draft payload', encoding='utf-8')
            with patch.object(site, 'DOCS', docs):
                site.build_current_guide_aliases()
                first = {p.relative_to(docs): p.read_bytes() for p in docs.rglob('*') if p.is_file()}
                site.build_current_guide_aliases()
                self.assertEqual(first, {p.relative_to(docs): p.read_bytes() for p in docs.rglob('*') if p.is_file()})
            current_pages = {page[0] for page in site.PAGES} | {'history'}
            for path, raw in first.items():
                self.assertEqual(path.suffix, '.html')
                target = '../../' + (path.stem if path.stem in current_pages else 'index') + '.html'
                text = raw.decode('utf-8')
                self.assertIn(f'href="{target}"', text)
                self.assertIn(f'content="0; url={target}"', text)
                self.assertIn('location.replace(', text)
                self.assertIn('location.hash', text)
                self.assertIn('name="robots" content="noindex"', text)
                self.assertNotIn('old draft payload', text)
                self.assertNotIn('오표기', text)

    def test_current_alias_cannot_delete_outside_its_published_subtree(self):
        with tempfile.TemporaryDirectory() as directory:
            docs = Path(directory) / 'docs'
            outside = docs / 'outside'
            outside.mkdir(parents=True)
            original = outside / 'keep.txt'
            original.write_text('preserve', encoding='utf-8')
            with patch.object(site, 'DOCS', docs), patch.object(site, 'CURRENT_GUIDE_ALIASES', ('../outside',)):
                with self.assertRaisesRegex(ValueError, 'escapes published versions'):
                    site.build_current_guide_aliases()
            self.assertEqual(original.read_text(encoding='utf-8'), 'preserve')

    def test_stable_and_history_do_not_mix(self):
        stable = (site.DOCS / 'sharing.html').read_text(encoding='utf-8')
        current = (site.DOCS / f'versions/{site.APP_VERSION}/sharing.html').read_text(encoding='utf-8')
        archived = (site.DOCS / 'versions/0.3.32/sharing.html').read_text(encoding='utf-8')
        previous = (site.DOCS / 'versions/0.3.31/index.html').read_text(encoding='utf-8')
        self.assertEqual(site.APP_VERSION, site.VERSIONS['authoringVersion'])
        self.assertIn(f'{site.APP_VERSION} · stable 안내', stable)
        self.assertIn('0.3.32 · 이전 기록', archived)
        self.assertIn('id="보내는-사람"', stable)
        self.assertIn('7일간', stable)
        self.assertNotIn('0.3.31에는', stable)
        self.assertIn('보존된 당시 안내', current)
        self.assertIn('0.3.31 · 이전 기록', previous)
        self.assertFalse((site.DOCS / 'versions/0.3.31/sharing.html').exists())

    def test_every_external_resource_opens_a_new_tab(self):
        from html.parser import HTMLParser
        class Links(HTMLParser):
            def handle_starttag(self, tag, attrs):
                values = dict(attrs)
                if tag != 'a' or not values.get('href'):
                    return
                if site.new_tab_attributes(values['href']):
                    assert values.get('target') == '_blank', values
                    assert 'noopener' in values.get('rel', ''), values
        for page in site.DOCS.rglob('*.html'):
            Links().feed(page.read_text(encoding='utf-8'))

    def test_current_images_follow_current_pixels_while_history_keeps_its_map(self):
        import hashlib
        import re
        source = (site.SOURCE / 'timeline.md').read_text(encoding='utf-8')
        name = re.search(r'!\[[^\]]*\]\(([^)]+glossary-depth\.png)\)', source).group(1).removeprefix('../')
        raw = (site.DOCS / name).read_bytes()
        current = site.current_assets()[name]
        self.assertEqual(current, 'assets/versioned/' + hashlib.sha256(raw).hexdigest() + '.png')
        self.assertIn(current, (site.DOCS / 'timeline.html').read_text(encoding='utf-8'))
        preserved = json.loads((site.HISTORY / '0.3.32/assets.json').read_text(encoding='utf-8'))['assets/examples/glossary-depth.png']
        self.assertIn(preserved, (site.DOCS / 'versions/0.3.32/timeline.html').read_text(encoding='utf-8'))


if __name__ == '__main__':
    unittest.main()
