from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE ="quote"
    UNORDERED_LIST ="unordered_list"
    ORDERED_LIST = "ordered_list"
    

def markdown_to_blocks(markdown: str) -> list[str]:
    split_by_line = [text.strip() for text in markdown.split("\n")]
    split_by_line.append("")
    
    block_list = []
    block_start_index = 0
    for i in range(len(split_by_line)):
        if split_by_line[i] == "":
            block_lines = split_by_line[block_start_index:i]
            if len(block_lines) != 0:
                block_list.append(block_lines)
            block_start_index = i +1
    
    return list(map("\n".join, block_list))

def block_to_block_type(block: str) -> str:
    if re.match(r"^#{1,6} ",block, re.MULTILINE):
        return BlockType.HEADING
    if re.match(r"^```[\s\S]*?```$", block):
        return BlockType.CODE
    if re.match("^(>.*(\n|$))+$", block):
        return BlockType.QUOTE
    if re.match(r"^((\*|-) .*(\n|$))+$", block):
        return BlockType.UNORDERED_LIST
    if __is_orderd_markdown_list(block):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
    

def __is_orderd_markdown_list(block: str) -> bool:
    lines = block.split("\n")
    for i in range(len(lines)):
        if not lines[i].startswith(f"{i+1}. "):
            return False
    return True


if __name__ == "__main__":
    markdown = """>dsfa
>adsfd
>    ```"""
    result = markdown_to_blocks(markdown)
    print(block_to_block_type(result[0]))
