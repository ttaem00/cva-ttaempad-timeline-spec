"""Catch omitted assets without letting the builder repair prepared output."""
import shutil
import tempfile
import unittest
from pathlib import Path

from check_published_site import check_directory

ROOT = Path(__file__).resolve().parent.parent


class PublishedSite(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        shutil.copytree(ROOT / 'docs', self.root / 'docs')

    def test_prepared_output_is_complete(self):
        self.assertGreater(check_directory(self.root), 100)

    def test_missing_current_image_is_rejected_before_rebuild(self):
        from html.parser import HTMLParser
        class Images(HTMLParser):
            def __init__(self):
                super().__init__()
                self.targets = []
            def handle_starttag(self, tag, attrs):
                values = dict(attrs)
                if tag == 'img' and values.get('src', '').startswith('assets/versioned/'):
                    self.targets.append(values['src'])
        parser = Images()
        parser.feed((self.root / 'docs/existing.html').read_text(encoding='utf-8'))
        self.assertTrue(parser.targets)
        (self.root / 'docs' / parser.targets[0]).unlink()
        with self.assertRaisesRegex(ValueError, 'missing published asset'):
            check_directory(self.root)

    def test_changed_image_is_rejected(self):
        image = next((self.root / 'docs/assets/versioned').glob('*.png'))
        image.write_bytes(image.read_bytes() + b'changed')
        with self.assertRaisesRegex(ValueError, 'differs from manifest'):
            check_directory(self.root)

    def test_unlisted_page_link_is_checked(self):
        (self.root / 'docs/extra.html').write_text('<img src="assets/missing.png">', encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'missing local link'):
            check_directory(self.root)


if __name__ == '__main__':
    unittest.main()
