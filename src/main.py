import os
import shutil

from copystatic import copy_files_recursive
import re
from markdow_to_htmlnode import markdown_to_html_node

STATIC_PATH: str = "./static/"
PUBLIC_PATH: str = "./public/"



def extract_title(markdown: str) -> str:
    match = re.search(r'^# (.+)', markdown, re.MULTILINE)
    if match:
        return match.group(1)
    raise ValueError("Markdown does not contain a title")


def generate_page(from_path: str, template_path: str, to_path: str) -> None:
    print(f"Generating page from {from_path} to {to_path} using {template_path}")
    with open(from_path, "r") as file:
        markdown = file.read()
    with open(template_path, "r") as file:
        template = file.read()
    
    title = extract_title(markdown)
    html = markdown_to_html_node(markdown).to_html()
    
    if not os.path.exists(os.path.dirname(to_path)):
        os.makedirs(os.path.dirname(to_path))
        
    with open(to_path, "w") as file:
        file.write(template.replace("{{ Title }}", title).replace("{{ Content }}", html))


def main():
    print("Deleting public directory...")
    if os.path.exists(PUBLIC_PATH):
        shutil.rmtree(PUBLIC_PATH)
    
    print("Copying static directory to public directory...")
    copy_files_recursive(STATIC_PATH, PUBLIC_PATH)
    
    generate_page("./content/index.md", "./template.html", "./public/index.html")
    
    
if __name__ == "__main__":
    main()