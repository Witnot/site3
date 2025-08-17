from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block: str) -> BlockType:
    lines = block.split("\n")
    
    # Check for heading: 1-6 # characters followed by a space
    if re.match(r"^#{1,6} ", lines[0]):
        return BlockType.HEADING
    
    # Check for code block: starts and ends with ```
    if lines[0].startswith("```") and lines[-1].endswith("```"):
        return BlockType.CODE
    
    # Check for quote: every line starts with >
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE
    
    # Check for unordered list: every line starts with "- "
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST
    
    # Check for ordered list: numbered starting from 1, incrementing
    ordered_match = True
    for i, line in enumerate(lines):
        if not re.match(rf"^{i+1}\. ", line):
            ordered_match = False
            break
    if ordered_match:
        return BlockType.ORDERED_LIST
    
    # Otherwise, it's a paragraph
    return BlockType.PARAGRAPH
