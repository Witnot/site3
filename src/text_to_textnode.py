from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter
from splitnodes import split_nodes_image, split_nodes_link
from text_to_html import text_node_to_html_node

def text_to_textnodes(text):
    # Start with the whole text as a single text node
    nodes = [TextNode(text, TextType.TEXT)]

    # Split code blocks first (`code`)
    new_nodes = []
    for node in nodes:
        new_nodes.extend(split_nodes_delimiter([node], "`", TextType.CODE))
    nodes = new_nodes

    # Split bold (**bold**)
    new_nodes = []
    for node in nodes:
        new_nodes.extend(split_nodes_delimiter([node], "**", TextType.BOLD))
    nodes = new_nodes

    # Split italic (_italic_)
    new_nodes = []
    for node in nodes:
        new_nodes.extend(split_nodes_delimiter([node], "_", TextType.ITALIC))
    nodes = new_nodes

    # Split images
    new_nodes = []
    for node in nodes:
        new_nodes.extend(split_nodes_image([node]))
    nodes = new_nodes

    # Split links
    new_nodes = []
    for node in nodes:
        new_nodes.extend(split_nodes_link([node]))
    nodes = new_nodes

    return nodes
def text_to_children(text):
    """
    Converts a raw text string into a list of LeafNodes representing
    inline markdown: bold, italic, code, links, images.
    """
    # Step 0: Normalize newlines for paragraph/inline content
    text = text.replace("\n", " ")

    # Step 1: Start with a single TextNode of type TEXT
    root_node = TextNode(text, TextType.TEXT)

    # Step 2: Apply splitting functions in order:
    # code, bold, italic, images, links
    nodes = [root_node]
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    return [text_node_to_html_node(n) for n in nodes]

