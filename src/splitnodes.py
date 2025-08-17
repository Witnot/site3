from regex import extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType


def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            # If not plain text, just append as-is
            new_nodes.append(node)
            continue

        matches = extract_markdown_images(node.text)
        if not matches:
            new_nodes.append(node)
            continue

        current_index = 0
        for alt_text, url in matches:
            # Find the start index of the current match
            match_index = node.text.find(f"![{alt_text}]({url})", current_index)
            # Text before the image
            if match_index > current_index:
                pre_text = node.text[current_index:match_index]
                if pre_text:
                    new_nodes.append(TextNode(pre_text, TextType.TEXT))
            # Add the image node
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
            # Move past the current match
            current_index = match_index + len(f"![{alt_text}]({url})")

        # Any remaining text after the last image
        if current_index < len(node.text):
            remaining_text = node.text[current_index:]
            if remaining_text:
                new_nodes.append(TextNode(remaining_text, TextType.TEXT))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            # If not plain text, just append as-is
            new_nodes.append(node)
            continue

        matches = extract_markdown_links(node.text)
        if not matches:
            new_nodes.append(node)
            continue

        current_index = 0
        for anchor_text, url in matches:
            match_index = node.text.find(f"[{anchor_text}]({url})", current_index)
            # Text before the link
            if match_index > current_index:
                pre_text = node.text[current_index:match_index]
                if pre_text:
                    new_nodes.append(TextNode(pre_text, TextType.TEXT))
            # Add the link node
            new_nodes.append(TextNode(anchor_text, TextType.LINK, url))
            current_index = match_index + len(f"[{anchor_text}]({url})")

        # Remaining text
        if current_index < len(node.text):
            remaining_text = node.text[current_index:]
            if remaining_text:
                new_nodes.append(TextNode(remaining_text, TextType.TEXT))

    return new_nodes
