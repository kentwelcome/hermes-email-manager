"""Dependency-free checks for the public static site."""
from html.parser import HTMLParser
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class Document(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.tags = []
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))

class SiteTests(unittest.TestCase):
    def test_pages(self):
        for name in ('index.html', 'privacy.html'):
            with self.subTest(page=name):
                doc = Document((ROOT / name).read_text())
                self.assertEqual(sum(t == 'h1' for t, _ in doc.tags), 1)
                self.assertIn(('html', {'lang': 'en'}), doc.tags)
                self.assertTrue(any(t == 'meta' and a.get('name') == 'viewport' for t, a in doc.tags))
                for tag, attrs in doc.tags:
                    self.assertNotIn(tag, ('script', 'iframe', 'form'))
                    for key in ('href', 'src'):
                        value = attrs.get(key, '')
                        if value.startswith('./'):
                            self.assertTrue((ROOT / value).exists(), value)
                self.assertTrue(any(a.get('href') == 'mailto:kentwelcome@gmail.com' for _, a in doc.tags))
    def test_domain(self):
        self.assertEqual((ROOT / 'CNAME').read_text().strip(), 'mail.kent-huang.dev')
    def test_privacy_disclosures(self):
        text = (ROOT / 'privacy.html').read_text()
        for term in ('AI providers', 'Slack', 'No fixed automatic deletion', 'Google Account third-party connections', 'GitHub Privacy Statement'):
            self.assertIn(term, text)

if __name__ == '__main__':
    unittest.main()
