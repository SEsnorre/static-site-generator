import os
import shutil

from copystatic import copy_files_recursive
from generate_pages import generate_pages_recursive

STATIC_PATH: str = "./static/"
PUBLIC_PATH: str = "./public/"
DIR_PATH_CONTENT: str = "./content/"
TEMPLATE_PATH: str = "./template.html"



def main():
    print("Deleting public directory...")
    if os.path.exists(PUBLIC_PATH):
        shutil.rmtree(PUBLIC_PATH)
    
    print("Copying static directory to public directory...")
    copy_files_recursive(STATIC_PATH, PUBLIC_PATH)
    
    generate_pages_recursive(DIR_PATH_CONTENT, TEMPLATE_PATH, PUBLIC_PATH)
    
    
if __name__ == "__main__":
    main()