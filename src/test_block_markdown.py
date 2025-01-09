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
        

if __name__ == "__main__":
    unittest.main()