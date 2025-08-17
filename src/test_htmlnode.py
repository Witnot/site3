# src/test_htmlnode.py
import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_empty(self):
        node = HTMLNode(tag='p', value='Hello')
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_single(self):
        node = HTMLNode(tag='a', value='Link', props={'href': 'https://example.com'})
        self.assertEqual(node.props_to_html(), ' href="https://example.com"')

    def test_props_to_html_multiple(self):
        node = HTMLNode(tag='div', props={'class': 'container', 'id': 'main'})
        # Order of attributes can vary; one simple way is to test for both possibilities
        result = node.props_to_html()
        expected1 = ' class="container" id="main"'
        expected2 = ' id="main" class="container"'
        self.assertIn(result, [expected1, expected2])

    def test_repr(self):
        child = HTMLNode(tag='span', value='Child')
        node = HTMLNode(tag='div', children=[child], props={'id': 'parent'})
        repr_str = repr(node)
        self.assertIn('HTMLNode', repr_str)
        self.assertIn('children=[HTMLNode', repr_str)
        self.assertIn("'id': 'parent'", repr_str)

if __name__ == "__main__":
    unittest.main()
