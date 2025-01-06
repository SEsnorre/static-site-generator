import re
from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            reslut.append(node)
            continue
        reslut = []
        splitted_text = node.text.split(delimiter)
        if len(splitted_text) % 2 == 0:
            raise Exception("Invalid Markdown")
        for i in range(len(splitted_text)):
            if splitted_text[i] == "":
                continue
            if i % 2 == 0:
                reslut.append(TextNode(splitted_text[i], TextType.TEXT))
            else:
                reslut.append(TextNode(splitted_text[i], text_type))
        new_nodes.extend(reslut)
    return new_nodes
        
        
def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    result = []
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    for match in matches:
        result.append((match[0], match[1]))
    return result

def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    result = []
    matches = re.findall(r"(?<!\!)\[(.*?)\]\((.*?)\)", text)
    result.extend([(match[0], match[1]) for match in matches])
    return result

def split_nodes_image(old_nodes: list[TextNode]):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        markdown_images = extract_markdown_images(node.text)

        if len(markdown_images) == 0:
            new_nodes.append(TextNode(node.text, TextType.TEXT))
            continue
        splitted_text = re.split(r"!\[.*?\]\(.*?\)", node.text)
        
        for i in range(len(splitted_text)):
            if splitted_text[i] == "":
                continue
            new_nodes.append(TextNode(splitted_text[i], TextType.TEXT))
            new_nodes.append(TextNode(markdown_images[i][0], TextType.IMAGE, markdown_images[i][1]))
    return new_nodes
        
def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        markdown_links = extract_markdown_links(node.text)

        if len(markdown_links) == 0:
            new_nodes.append(TextNode(node.text, TextType.TEXT))
            continue
        splitted_text = re.split(r"(?<!\!)\[.*?\]\(.*?\)", node.text)

        for i in range(len(splitted_text)):
            if splitted_text[i] == "":
                continue
            new_nodes.append(TextNode(splitted_text[i], TextType.TEXT))
            new_nodes.append(TextNode(markdown_links[i][0], TextType.LINK, markdown_links[i][1]))
    return new_nodes