import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_raw_text(self):
        node = LeafNode(None, "Just text")
        self.assertEqual(node.to_html(), "Just text")

    def test_leaf_to_html_with_props(self):
        node = LeafNode("a", "Click me", {"href": "https://example.com"})
        self.assertEqual(node.to_html(), '<a href="https://example.com">Click me</a>')

    def test_leaf_no_value_raises(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None)

    def test_leaf_to_html_empty_tag(self):
        node = LeafNode("span", "inline text", {"class": "highlight"})
        self.assertEqual(node.to_html(), '<span class="highlight">inline text</span>')

if __name__ == "__main__":
    unittest.main()
