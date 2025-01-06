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
        