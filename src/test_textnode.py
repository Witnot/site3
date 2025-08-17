import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_equal_nodes(self):
        node1 = TextNode("Hello", TextType.TEXT, None)
        node2 = TextNode("Hello", TextType.TEXT, None)
        self.assertEqual(node1, node2)  # Should be equal

    def test_different_text(self):
        node1 = TextNode("Hello", TextType.TEXT, None)
        node2 = TextNode("World", TextType.TEXT, None)
        self.assertNotEqual(node1, node2)  # Text differs

    def test_different_text_type(self):
        node1 = TextNode("Hello", TextType.TEXT, None)
        node2 = TextNode("Hello", TextType.BOLD, None)
        self.assertNotEqual(node1, node2)  # TextType differs

    def test_different_url(self):
        node1 = TextNode("Click me", TextType.LINK, "http://example.com")
        node2 = TextNode("Click me", TextType.LINK, "http://other.com")
        self.assertNotEqual(node1, node2)  # URLs differ

    def test_url_none_vs_value(self):
        node1 = TextNode("Click me", TextType.LINK, None)
        node2 = TextNode("Click me", TextType.LINK, "http://example.com")
        self.assertNotEqual(node1, node2)  # One URL is None

if __name__ == "__main__":
    unittest.main()