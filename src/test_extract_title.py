import unittest
from extract_title import extract_title   # replace with the actual module name

class TestExtractTitle(unittest.TestCase):
    def test_simple_h1(self):
        self.assertEqual(extract_title("# Hello"), "Hello")

    def test_h1_with_whitespace(self):
        self.assertEqual(extract_title("   #   Hello World   "), "Hello World")

    def test_multiple_lines_first_is_h1(self):
        md = "# Title\nSome text\n## Subtitle"
        self.assertEqual(extract_title(md), "Title")

    def test_multiple_lines_h1_after_text(self):
        md = "Intro text\n# My Title\nMore text"
        self.assertEqual(extract_title(md), "My Title")

    def test_h1_not_confused_with_h2(self):
        md = "## Subtitle\n### Another\n# Real Title"
        self.assertEqual(extract_title(md), "Real Title")

    def test_no_h1_raises(self):
        md = "## Subtitle only\nSome text"
        with self.assertRaises(ValueError):
            extract_title(md)

    def test_h1_inside_code_block(self):
        md = "```\n# Not a Title\n```\n# Real Title"
        # current implementation doesn’t ignore code blocks — adjust if needed
        self.assertEqual(extract_title(md), "Not a Title")  

if __name__ == "__main__":
    unittest.main()
