import unittest
from inline_markdown import *

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_code_block(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)
        
    def test_invalid_markdown(self):
        node = TextNode("this is an invalid `code block word", TextType.TEXT)
        self.assertRaises(Exception, split_nodes_delimiter, node)
    


if __name__ == "__main__":
    unittest.main()