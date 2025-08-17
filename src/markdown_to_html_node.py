import re
import textwrap
from BlockType import BlockType, block_to_block_type
from markdown_to_blocks import markdown_to_blocks
from parentnode import ParentNode
from textnode import TextNode, TextType
from text_to_html import text_node_to_html_node
from leafnode import LeafNode
from text_to_textnode import text_to_textnodes, text_to_children
from htmlnode import HTMLNode

def markdown_to_html_node(markdown: str) -> HTMLNode:
    parent_children = []
    blocks = markdown_to_blocks(markdown)

    for block in blocks:
        block_type = block_to_block_type(block)
        block_children = []

        if block_type == BlockType.PARAGRAPH:
            for tn in text_to_textnodes(block):
                block_children.append(text_node_to_html_node(tn))
            if block_children:  # Only create paragraph if we have content
                parent_children.append(ParentNode("p", block_children))

        elif block_type == BlockType.HEADING:
            lines = block.splitlines()
            for line in lines:
                level = 0
                while level < len(line) and line[level] == "#":
                    level += 1
                heading_text = line[level:].strip()
                if heading_text:  # Only create heading if there's text
                    children = [text_node_to_html_node(tn) for tn in text_to_textnodes(heading_text)]
                    if children:  # Only create heading if we have children
                        parent_children.append(ParentNode(f"h{level}", children))

        elif block_type == BlockType.CODE:
            lines = block.splitlines()[1:-1]  # remove first and last ``` lines
            code_text = textwrap.dedent("\n".join(lines)) + "\n"
            code_node = LeafNode("code", code_text)
            parent_children.append(ParentNode("pre", [code_node]))

        elif block_type == BlockType.QUOTE:
            lines = []
            for line in block.splitlines():
                line_stripped = line.strip()
                if line_stripped.startswith("> "):
                    lines.append(line_stripped[2:])  # Remove "> " 
                elif line_stripped == ">":
                    lines.append("")  # Empty quote line becomes empty string
            if lines:  # Only process if we have quote lines
                # Join all quote lines with spaces, filtering out empty ones
                quote_parts = [line for line in lines if line.strip()]
                quote_text = " ".join(quote_parts).strip()
                if quote_text:  # Only create quote if there's content
                    # Create text nodes without wrapping in <p>
                    block_children = []
                    for tn in text_to_textnodes(quote_text):
                        block_children.append(text_node_to_html_node(tn))
                    if block_children:
                        parent_children.append(ParentNode("blockquote", block_children))

        elif block_type == BlockType.UNORDERED_LIST:
            lines = block.strip().splitlines()
            for line in lines:
                line = line.strip()
                if line.startswith("- "):
                    item_text = line[2:].strip()  # remove "- "
                    if item_text:  # Only create list item if there's content
                        item_children = [text_node_to_html_node(tn) for tn in text_to_textnodes(item_text)]
                        if item_children:  # Only create li if we have children
                            block_children.append(ParentNode("li", item_children))
            if block_children:  # Only create ul if we have list items
                parent_children.append(ParentNode("ul", block_children))

        elif block_type == BlockType.ORDERED_LIST:
            lines = block.strip().split("\n")
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                # Find the ". " separator
                dot_index = line.find(". ")
                if dot_index != -1:
                    content = line[dot_index + 2:]  # Skip ". "
                    if content.strip():  # Only create list item if there's content
                        item_children = [text_node_to_html_node(tn) for tn in text_to_textnodes(content)]
                        if item_children:  # Only create li if we have children
                            block_children.append(ParentNode("li", item_children))
            if block_children:  # Only create ol if we have list items
                parent_children.append(ParentNode("ol", block_children))

    # Ensure we always have at least one child for the root div
    if not parent_children:
        # If no content, create an empty paragraph
        parent_children.append(ParentNode("p", [LeafNode(None, "")]))
    
    return ParentNode("div", parent_children)