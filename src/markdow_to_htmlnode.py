from block_markdown import markdown_to_blocks, BlockType, block_to_block_type
from htmlnode import HTMLNode, ParentNode, LeafNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node

def markdown_to_html_node(markdown: str) -> ParentNode:
    markdown_blocks = markdown_to_blocks(markdown_to_blocks)
    parent_html_node = ParentNode("div", [])
    
    for block in markdown_blocks:
        parent_html_node.children.append(text_to_children(block))
        
    
def text_to_children(text:str) -> HTMLNode:
    block_type = block_to_block_type(text)
    match block_type:
        case BlockType.PARAGRAPH:
            return paragraph_to_html_node(text)
        case BlockType.HEADING:
            return header_to_html_node(text)
        case BlockType.CODE:
            return code_to_html_node(text)
        case BlockType.QUOTE:
            return quote_to_html_node(text)
        case BlockType.UNORDERED_LIST | BlockType.ORDERED_LIST :
            return list_to_html_node(text, block_type)
        case _:
            raise ValueError("Unknown block type")
        
def list_to_html_node(text: str, type: BlockType.value) -> HTMLNode:
    lines = [x[2:] for x in text.split("\n")]
    list_tag = "ol" if type == BlockType.ORDERED_LIST else "ul"
    list_node = ParentNode(list_tag, [])
    for line in lines:
        list_node.children.append(LeafNode("li", line))
    return list_node
        
def quote_to_html_node(text: str) -> HTMLNode:
    quote_text = " ".joint([x[2:] for x in text.split("\n")])
    return LeafNode("blockquote", quote_text)
  
def code_to_html_node(text: str) -> HTMLNode:
    code_text = text.split("\n")[1:-1]
    return ParentNode("pre", [LeafNode("code", code_text)])
            
def header_to_html_node(text: str) -> HTMLNode:
    splited_text = text.split(maxsplit=1)
    header_type = len(splited_text[0])
    header_value = splited_text[1]
    return LeafNode(f"h{header_type}", header_value)

def paragraph_to_html_node(text: str) -> HTMLNode:
    text_nodes = text_to_textnodes(text)
    p_node = ParentNode("p", [])
    for node in text_nodes:
        p_node.children.append(text_node_to_html_node(node))
    return p_node