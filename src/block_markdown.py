from enum import Enum

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
                block.append(block_lines)
            block_start_index = i +1
    
    return list(map("\n".join, block_list))

def block_to_block_type(block: str) -> str:
    pass

if __name__ == "__main__":
    markdown = """
    
    # This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.




* This is the first list item in a list block
* This is a list item
* This is another list item"""
    result = markdown_to_blocks(markdown)
    print(result)
