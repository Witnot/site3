def extract_title(markdown: str) -> str:
    """
    Extracts the first H1 header (# ...) from a markdown string.
    Returns the title text without the leading # and surrounding whitespace.
    Raises ValueError if no H1 header is found.
    """
    for line in markdown.splitlines():
        line = line.strip()
        if line.startswith("# "):  # only H1, not ## or ###
            return line[2:].strip()
    raise ValueError("No H1 header found in markdown")
