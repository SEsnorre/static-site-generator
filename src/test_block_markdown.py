import unittest
from block_markdown import *

class TestMarkdownToBlocks(unittest.TestCase):
    def test_standard_markdown(self):
        markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""
        result = markdown_to_blocks(markdown)
        expected = [
            '# This is a heading',
            'This is a paragraph of text. It has some **bold** and *italic* words inside of it.',
            '* This is the first list item in a list block\n* This is a list item\n* This is another list item'
        ]
        self.assertEqual(result, expected)
        
    def test_standard_markdown_with_multiline(self):
        markdown = """
        
        # This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.




* This is the first list item in a list block                
* This is a list item
* This is another list item"""
        result = markdown_to_blocks(markdown)
        expected = [
            '# This is a heading',
            'This is a paragraph of text. It has some **bold** and *italic* words inside of it.',
            '* This is the first list item in a list block\n* This is a list item\n* This is another list item'
        ]
        self.assertEqual(result, expected)
        

class TestBlockToBlockType(unittest.TestCase):
    def test_heading_block(self):
        block_text = "# This is a heading"
        block_text2 = "###### This is a 6 Hashtag Heading"
        self.assertEqual(block_to_block_type(block_text), BlockType.HEADING)
        self.assertEqual(block_to_block_type(block_text2), BlockType.HEADING)
        
    def test_code_block(self):
        block_text = "```This is a code```"
        block_text2 = "``` This is multiline \ncode\npass```"
        self.assertEqual(block_to_block_type(block_text), BlockType.CODE)
        self.assertEqual(block_to_block_type(block_text2), BlockType.CODE)
        
    def test_quote_block(self):
        block_text = "> This is a quote```"
        block_text2 = "> This is multiline \n> quote\n> pass```"
        self.assertEqual(block_to_block_type(block_text), BlockType.QUOTE)
        self.assertEqual(block_to_block_type(block_text2), BlockType.QUOTE)
        
    def test_unordered_list_block(self):
        block_text = "* This is a single line list```"
        block_text2 = "- This is a single line list```"
        block_text3 = "* This is multiline \n- list\n* pass```"
        self.assertEqual(block_to_block_type(block_text), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type(block_text2), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type(block_text3), BlockType.UNORDERED_LIST)
        
    def test_ordered_list_block(self):
        block_text = "1. This is a single line list```"
        block_text2 = "1. This is multiline \n2. list\n3. pass```"
        self.assertEqual(block_to_block_type(block_text), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type(block_text2), BlockType.ORDERED_LIST)
        
    def test_other_return_paragraph(self):
        input_list = ["2. This is a single line list```",
        "1. This is multiline \n1. list\n3. pass```",
        "This is multiline \n- list\n* pass```",
        "This is multiline \n> quote\n> pass```",
        "` This is multiline \ncode\npass```",
        "######## This is a 6 Hashtag Heading",
        "Thest of\nmultiline paragrapg\nbock"]
        for item in input_list:
            self.assertEqual(block_to_block_type(item), BlockType.PARAGRAPH)
        
        
        
if __name__ == "__main__":
    unittest.main()