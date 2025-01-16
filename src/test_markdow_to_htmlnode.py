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
        
class TestHeaderToHtmlNode(unittest.TestCase):
    def test_standard_header(self):
        test_text = ["# header1",
                "### header3",
                "###### Header 6 with more text"
                ]
             
        expected = [LeafNode("h1", "header1"),
                    LeafNode("h3", "header3"),
                    LeafNode("h6", "Header 6 with more text")
                    ]
        
        for i in range(len(test_text)):
            self.assertEqual(header_to_html_node(test_text[i]), expected[i])
        
if __name__ == "__main__":
    unittest.main()