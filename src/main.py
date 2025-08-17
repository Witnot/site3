import os
import sys
import shutil
from copy_static import copy_static_to_public
from generate_pages_recursive import generate_pages_recursive

def main():
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # Get basepath from command line argument, default to "/"
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
        # Ensure basepath starts and ends with "/"
        if not basepath.startswith("/"):
            basepath = "/" + basepath
        if not basepath.endswith("/"):
            basepath = basepath + "/"
    
    static_dir = os.path.join(project_root, "static")
    docs_dir = os.path.join(project_root, "docs")  # Changed from public to docs
    content_dir = os.path.join(project_root, "content")
    template_file = os.path.join(project_root, "template.html")
    
    print(f"🌐 Using basepath: {basepath}")
    
    # 1. Delete anything in the docs directory
    if os.path.exists(docs_dir):
        print("🗑️  Clearing docs directory...")
        shutil.rmtree(docs_dir)
    
    # 2. Copy static files
    print("📂 Copying static files...")
    copy_static_to_public(static_dir, docs_dir)  # Changed destination to docs_dir
    
    # 3. Generate all pages recursively
    print("📝 Generating pages recursively...")
    generate_pages_recursive(content_dir, template_file, docs_dir, basepath)  # Changed destination to docs_dir
    
    print("✅ Site generation complete!")

if __name__ == "__main__":
    main()