"""Release boundaries and reading-site behavior contracts, without a product parser."""
import copy
import json
import shutil
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import build_site as site
from capture_guide_release import capture


class GuideVersions(unittest.TestCase):
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
        with tempfile.TemporaryDirectory(dir=scratch) as directory:
            history = Path(directory)
            shutil.copytree(site.HISTORY, history, dirs_exist_ok=True)
            target = history / '0.3.32/source/sharing.md'
            target.write_text('changed', encoding='utf-8')
            with patch.object(site, 'HISTORY', history), self.assertRaisesRegex(ValueError, 'preserved version changed'):
                site.verify_history()

    def test_stable_and_history_do_not_mix(self):
        stable = (site.DOCS / 'sharing.html').read_text(encoding='utf-8')
        current = (site.DOCS / 'versions/0.3.32/sharing.html').read_text(encoding='utf-8')
        previous = (site.DOCS / 'versions/0.3.31/index.html').read_text(encoding='utf-8')
        self.assertEqual(site.APP_VERSION, '0.3.32')
        self.assertIn('0.3.32 · stable 안내', stable)
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
        name = 'assets/examples/glossary-depth.png'
        raw = (site.DOCS / name).read_bytes()
        current = site.current_assets()[name]
        self.assertEqual(current, 'assets/versioned/' + hashlib.sha256(raw).hexdigest() + '.png')
        self.assertIn(current, (site.DOCS / 'timeline.html').read_text(encoding='utf-8'))
        preserved = json.loads((site.HISTORY / '0.3.32/assets.json').read_text(encoding='utf-8'))[name]
        self.assertIn(preserved, (site.DOCS / 'versions/0.3.32/timeline.html').read_text(encoding='utf-8'))


if __name__ == '__main__':
    unittest.main()
