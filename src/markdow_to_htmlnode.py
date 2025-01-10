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
            pass

def paragraph_to_html_node(text: str) -> HTMLNode:
    text_nodes = text_to_textnodes(text)
    p_node = ParentNode("p", [])
    for node in text_nodes:
        p_node.children.append(text_node_to_html_node(node))
    return p_node