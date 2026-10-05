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
    def test_history_is_intact_and_cannot_be_recaptured(self):
        site.verify_history()
        with self.assertRaisesRegex(ValueError, 'already preserved'):
            capture('0.3.31', 'HEAD')

    def test_unannounced_promotion_is_rejected(self):
        metadata = copy.deepcopy(site.VERSIONS)
        metadata['authoringVersion'] = '0.3.32'
        with patch.object(site, 'VERSIONS', metadata), self.assertRaisesRegex(ValueError, 'promote explicitly'):
            site.verify_history()

    def test_preserved_source_tampering_is_rejected(self):
        scratch = site.ROOT / '.runtime'
        scratch.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=scratch) as directory:
            history = Path(directory)
            shutil.copytree(site.HISTORY / '0.3.32', history / '0.3.32')
            target = history / '0.3.32/source/sharing.md'
            target.write_text('changed', encoding='utf-8')
            with patch.object(site, 'HISTORY', history), self.assertRaisesRegex(ValueError, 'preserved version changed'):
                site.verify_history()

    def test_stable_and_preview_do_not_mix(self):
        stable = (site.DOCS / 'sharing.html').read_text(encoding='utf-8')
        preview = (site.DOCS / 'versions/0.3.32/sharing.html').read_text(encoding='utf-8')
        self.assertIn('0.3.31에는', stable)
        self.assertNotIn('id="보내는-사람"', stable)
        self.assertIn('0.3.32 미리보기', preview)
        self.assertIn('현재 stable은 0.3.31', preview)
        self.assertIn('7일간', preview)

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


if __name__ == '__main__':
    unittest.main()
