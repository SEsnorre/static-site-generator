import re
from textnode import TextType, TextNode

def split_nodes_delimiter(delimiter: str, text_type: TextType):
    def split_nodes(old_nodes: list[TextNode]) -> list[TextNode]:
        new_nodes = []
        for node in old_nodes:
            if node.text_type != TextType.TEXT:
                new_nodes.append(node)
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
    return split_nodes

split_bold_nodes = split_nodes_delimiter("**", TextType.BOLD)
split_italic_nodes = split_nodes_delimiter("*", TextType.ITALIC)
split_inlinecode_nodes = split_nodes_delimiter("`", TextType.CODE)
        
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
            if splitted_text[i] != "":
                new_nodes.append(TextNode(splitted_text[i], TextType.TEXT))
            if i < len(markdown_images):
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
            if splitted_text[i] != "":
                new_nodes.append(TextNode(splitted_text[i], TextType.TEXT))
            if i < len(markdown_links):
                new_nodes.append(TextNode(markdown_links[i][0], TextType.LINK, markdown_links[i][1]))
    return new_nodes


def text_to_textnodes(text: str) -> list[TextNode]:
    node = TextNode(text, TextType.TEXT)
    by_link = split_nodes_link([node])
    by_image = split_nodes_image(by_link)
    by_code = split_inlinecode_nodes(by_image)
    by_bold = split_bold_nodes(by_code)
    by_italic = split_italic_nodes(by_bold)
    return by_italic