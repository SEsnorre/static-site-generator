import re
import os
from markdow_to_htmlnode import markdown_to_html_node

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
        

def generate_pages_recursive(from_path: str, template_path: str, to_path: str) -> None:
    print(f"Generating pages from {from_path} to {to_path} using {template_path}")
    
    if os.path.isdir(from_path):
        for item in os.listdir(from_path):
            s = os.path.join(from_path, item)
            d = os.path.join(to_path, item)
            if os.path.isdir(s):
                generate_pages_recursive(s, template_path, d)
            elif s.endswith(".md"):
                generate_page(s, template_path, d.replace(".md", ".html"))
    elif from_path.endswith(".md"):
        generate_page(from_path, template_path, to_path)
    else:
        raise ValueError(f"Invalid file {from_path}")