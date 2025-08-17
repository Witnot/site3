import unittest
from regex import extract_markdown_images, extract_markdown_links
class TestMarkdownExtraction(unittest.TestCase):

    # Image tests
    def test_extract_single_image(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_multiple_images(self):
        text = "![first](https://a.com/1.png) and ![second](https://b.com/2.png)"
        matches = extract_markdown_images(text)
        self.assertListEqual([
            ("first", "https://a.com/1.png"),
            ("second", "https://b.com/2.png")
        ], matches)

    def test_extract_no_images(self):
        text = "There are no images here."
        matches = extract_markdown_images(text)
        self.assertListEqual([], matches)

    # Link tests
    def test_extract_single_link(self):
        matches = extract_markdown_links(
            "This is a [link](https://example.com)"
        )
        self.assertListEqual([("link", "https://example.com")], matches)

    def test_extract_multiple_links(self):
        text = "Check [Google](https://google.com) and [GitHub](https://github.com)"
        matches = extract_markdown_links(text)
        self.assertListEqual([
            ("Google", "https://google.com"),
            ("GitHub", "https://github.com")
        ], matches)

    def test_extract_no_links(self):
        text = "No links here!"
        matches = extract_markdown_links(text)
        self.assertListEqual([], matches)

    def test_ignore_images_in_links(self):
        text = "![image](https://img.com/a.png) and [link](https://link.com)"
        link_matches = extract_markdown_links(text)
        image_matches = extract_markdown_images(text)
        self.assertListEqual([("link", "https://link.com")], link_matches)
        self.assertListEqual([("image", "https://img.com/a.png")], image_matches)
