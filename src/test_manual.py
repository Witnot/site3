import unittest
from textnode import TextNode, TextType
from regex import extract_markdown_images, extract_markdown_links
from splitnodes import split_nodes_link, split_nodes_image

from textnode import TextNode, TextType
from text_to_textnode import text_to_textnodes  # replace with the actual module name
from markdown_to_blocks import markdown_to_blocks
from BlockType import block_to_block_type
print(block_to_block_type("# Heading 1"))  # BlockType.HEADING
print(block_to_block_type("```python\nprint('hello')\n```"))  # BlockType.CODE
print(block_to_block_type("> This is a quote"))  # BlockType.QUOTE
print(block_to_block_type("- Item 1\n- Item 2"))  # BlockType.UNORDERED_LIST
print(block_to_block_type("1. First\n2. Second"))  # BlockType.ORDERED_LIST
print(block_to_block_type("Just a normal paragraph."))  # BlockType.PARAGRAPH


class splitnodes(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )


