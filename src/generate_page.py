import os
from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title

def generate_page(from_path, template_path, dest_path, basepath="/"):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # Read the markdown file
    with open(from_path, "r", encoding="utf-8") as f:
        markdown_content = f.read()

    # Read the template file
    with open(template_path, "r", encoding="utf-8") as f:
        template_content = f.read()

    # Convert markdown to HTML
    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()

    # Extract the title
    title = extract_title(markdown_content)

    # Replace placeholders
    final_html = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_content)
    
    # Replace absolute paths with basepath
    if basepath != "/":
        # For non-root basepath, replace href="/ with href="{basepath} and src="/ with src="{basepath}
        final_html = final_html.replace('href="/', f'href="{basepath}')
        final_html = final_html.replace('src="/', f'src="{basepath}')

    # Ensure destination directory exists
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    # Write the final HTML page
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(final_html)