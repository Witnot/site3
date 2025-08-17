import re

def extract_markdown_images(text):
    # Markdown images are like ![alt](url)
    pattern = r'!\[([^\]]+)\]\(([^)]+)\)'
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    # Markdown links are like [anchor](url), but not preceded by !
    pattern = r'(?<!\!)\[([^\]]+)\]\(([^)]+)\)'
    matches = re.findall(pattern, text)
    return matches
