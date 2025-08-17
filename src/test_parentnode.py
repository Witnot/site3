import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_multiple_children_mixed(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold"),
                LeafNode(None, " and "),
                LeafNode("i", "italics"),
            ],
        )
        self.assertEqual(node.to_html(), "<p><b>Bold</b> and <i>italics</i></p>")

    def test_parent_with_props(self):
        node = ParentNode(
            "div",
            [LeafNode("span", "child")],
            props={"id": "main", "class": "container"},
        )
        # relies on insertion order of dict literal (Python 3.7+)
        self.assertEqual(
            node.to_html(),
            '<div id="main" class="container"><span>child</span></div>',
        )

    def test_child_with_props(self):
        node = ParentNode(
            "p",
            [LeafNode("a", "link", {"href": "https://example.com", "target": "_blank"})],
        )
        self.assertEqual(
            node.to_html(),
            '<p><a href="https://example.com" target="_blank">link</a></p>',
        )

    def test_raw_text_children(self):
        node = ParentNode("div", [LeafNode(None, "hello "), LeafNode("b", "world")])
        self.assertEqual(node.to_html(), "<div>hello <b>world</b></div>")

    def test_init_raises_without_tag(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("span", "x")])

    def test_init_raises_without_children(self):
        with self.assertRaises(ValueError):
            ParentNode("div", None)

    def test_to_html_raises_with_empty_children_list(self):
        node = ParentNode("div", [])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_deep_nesting(self):
        deep = ParentNode(
            "section",
            [
                ParentNode(
                    "article",
                    [
                        ParentNode(
                            "p",
                            [
                                LeafNode(None, "A "),
                                LeafNode("i", "deeply"),
                                LeafNode(None, " nested "),
                                LeafNode("b", "tree"),
                                LeafNode(None, "."),
                            ],
                        )
                    ],
                )
            ],
        )
        self.assertEqual(
            deep.to_html(),
            "<section><article><p>A <i>deeply</i> nested <b>tree</b>.</p></article></section>",
        )

if __name__ == "__main__":
    unittest.main()
