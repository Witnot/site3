
import os
import shutil
from copy_static import copy_static_to_public
from generate_pages_recursive import generate_pages_recursive

def main():
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    static_dir = os.path.join(project_root, "static")
    public_dir = os.path.join(project_root, "public")
    content_dir = os.path.join(project_root, "content")
    template_file = os.path.join(project_root, "template.html")
    
    # 1. Delete anything in the public directory
    if os.path.exists(public_dir):
        print("🗑️  Clearing public directory...")
        shutil.rmtree(public_dir)
    
    # 2. Copy static files
    print("📂 Copying static files...")
    copy_static_to_public(static_dir, public_dir)
    
    # 3. Generate all pages recursively
    print("📝 Generating pages recursively...")
    generate_pages_recursive(content_dir, template_file, public_dir)
    
    print("✅ Site generation complete!")

if __name__ == "__main__":
    main()