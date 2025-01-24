import os
import shutil

def copy_files_recursive(src: str, dest: str) -> None:
    if not os.path.exists(dest):
        os.makedirs(dest)
    if not os.path.exists(src):
        raise FileNotFoundError(f"Source directory {src} does not exist")
    
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dest, item)
        if os.path.isdir(s):
            copy_files_recursive(s, d)
        else:
            shutil.copy2(s, d)