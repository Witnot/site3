import os
import shutil

def copy_static_to_public(src_dir, dst_dir):
    """
    Recursively copies everything from src_dir into dst_dir.
    Clears dst_dir before copying.
    Logs every file copied.
    """

    # Step 1: clear destination directory
    if os.path.exists(dst_dir):
        shutil.rmtree(dst_dir)
    os.makedirs(dst_dir)

    # Step 2: recursive copy
    def recursive_copy(src, dst):
        for item in os.listdir(src):
            src_path = os.path.join(src, item)
            dst_path = os.path.join(dst, item)

            if os.path.isdir(src_path):
                os.makedirs(dst_path, exist_ok=True)
                print(f"📂 Creating directory: {dst_path}")
                recursive_copy(src_path, dst_path)  # recursive step
            else:
                shutil.copy2(src_path, dst_path)
                print(f"📄 Copied file: {src_path} -> {dst_path}")

    recursive_copy(src_dir, dst_dir)