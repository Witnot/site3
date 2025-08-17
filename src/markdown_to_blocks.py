def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = []
    lines = markdown.split("\n")
    i = 0
    
    while i < len(lines):
        line = lines[i].strip()
        
        # Skip empty lines
        if not line:
            i += 1
            continue
            
        # Handle code blocks (with or without indentation)
        if line.startswith("```"):
            code_lines = []
            code_lines.append("```")  # Always start with ```
            i += 1
            while i < len(lines):
                current_line = lines[i]
                if current_line.strip().endswith("```"):
                    code_lines.append("```")  # Always end with ```
                    break
                else:
                    # Preserve original indentation for code content
                    code_lines.append(current_line)
                i += 1
            blocks.append("\n".join(code_lines))
            
        # Handle ordered lists (lines starting with number + ". ")
        elif line and line[0].isdigit() and ". " in line:
            list_lines = [lines[i]]
            i += 1
            while i < len(lines):
                next_line = lines[i].strip()
                if next_line and next_line[0].isdigit() and ". " in next_line:
                    list_lines.append(lines[i])
                    i += 1
                elif not next_line:  # Empty line - check if list continues after
                    # Look ahead to see if there's another list item
                    j = i + 1
                    while j < len(lines) and not lines[j].strip():
                        j += 1
                    if j < len(lines) and lines[j].strip() and lines[j].strip()[0].isdigit() and ". " in lines[j].strip():
                        i = j  # Skip empty lines and continue with list
                        continue
                    else:
                        break  # End of list
                else:
                    break  # End of list
            blocks.append("\n".join(list_lines))
            continue
            
        # Handle unordered lists (lines starting with "- ")
        elif line.startswith("- "):
            list_lines = [lines[i]]
            i += 1
            while i < len(lines):
                next_line = lines[i].strip()
                if next_line.startswith("- "):
                    list_lines.append(lines[i])
                    i += 1
                elif not next_line:  # Empty line - check if list continues after
                    # Look ahead to see if there's another list item
                    j = i + 1
                    while j < len(lines) and not lines[j].strip():
                        j += 1
                    if j < len(lines) and lines[j].strip().startswith("- "):
                        i = j  # Skip empty lines and continue with list
                        continue
                    else:
                        break  # End of list
                else:
                    break  # End of list
            blocks.append("\n".join(list_lines))
            continue
            
        # Handle quotes (lines starting with "> ")
        elif line.startswith("> "):
            quote_lines = [lines[i]]
            i += 1
            while i < len(lines):
                next_line = lines[i].strip()
                if next_line.startswith("> "):
                    quote_lines.append(lines[i])
                    i += 1
                elif not next_line:  # Empty line - check if quote continues after
                    # Look ahead to see if there's another quote line
                    j = i + 1
                    while j < len(lines) and not lines[j].strip():
                        j += 1
                    if j < len(lines) and lines[j].strip().startswith("> "):
                        i = j  # Skip empty lines and continue with quote
                        continue
                    else:
                        break  # End of quote
                else:
                    break  # End of quote
            blocks.append("\n".join(quote_lines))
            continue
            
        # Handle headings and paragraphs
        else:
            # For paragraphs, collect consecutive non-empty lines that aren't special blocks
            paragraph_lines = [lines[i].strip()]
            i += 1
            while i < len(lines):
                next_line = lines[i].strip()
                # Stop if we hit an empty line or start of a special block
                if (not next_line or 
                    next_line.startswith("```") or 
                    next_line.startswith("- ") or 
                    next_line.startswith("> ") or 
                    next_line.startswith("#") or
                    (next_line and next_line[0].isdigit() and ". " in next_line)):
                    break
                paragraph_lines.append(lines[i].strip())
                i += 1
            # Join paragraph lines with spaces for proper text flow
            blocks.append(" ".join(paragraph_lines))
            continue
            
        i += 1
    
    return blocks