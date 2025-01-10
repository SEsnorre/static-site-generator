import unittest
from markdow_to_htmlnode import *
from htmlnode import *

class TestParagraphToHtmlNode(unittest.TestCase):
    def test_paragraph(self):
        text = "aaaa\nklsdj"
        result = text_to_children(text)
        expected = ParentNode("p", [LeafNode(None, "aaaa\nklsdj")])
        self.assertEqual(result, expected)
        
        
    def test_text_with_inline_md(self):
        text = "this is `code` and **bold** and *italic*"
        result = text_to_children(text)
        expected = ParentNode("p",[
            LeafNode(None, "this is "),
            LeafNode("code", "code"),
            LeafNode(None, " and "),
            LeafNode("b", "bold"),
            LeafNode(None, " and "),
            LeafNode("i", "italic")
            ])
        self.assertEqual(result, expected)
        
if __name__ == "__main__":
    unittest.main()