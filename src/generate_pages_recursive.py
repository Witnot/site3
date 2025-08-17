import os
from generate_page import generate_page

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    """
    Recursively crawl through the content directory and generate HTML pages
    for all markdown files found, maintaining the same directory structure
    in the destination directory.
    
    Args:
        dir_path_content: Path to the content directory containing markdown files
        template_path: Path to the HTML template file
        dest_dir_path: Path to the destination directory for generated HTML files
    """
    # Check if the content directory exists
    if not os.path.exists(dir_path_content):
        print(f"Content directory {dir_path_content} does not exist")
        return
    
    # Walk through all directories and files in the content directory
    for root, dirs, files in os.walk(dir_path_content):
        # Process each file in the current directory
        for file in files:
            # Only process markdown files
            if file.endswith('.md'):
                # Get the full path to the markdown file
                markdown_file_path = os.path.join(root, file)
                
                # Calculate the relative path from the content directory
                relative_path = os.path.relpath(markdown_file_path, dir_path_content)
                
                # Change the file extension from .md to .html
                html_filename = os.path.splitext(relative_path)[0] + '.html'
                
                # Create the destination path
                dest_file_path = os.path.join(dest_dir_path, html_filename)
                
                # Generate the page
                print(f"Generating page: {relative_path} -> {html_filename}")
                generate_page(markdown_file_path, template_path, dest_file_path)