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
            
            
class TestMarkdownToHtmlNode(unittest.TestCase):
    def test_markdown_to_html_node(self):
        markdown = "# Header\n\nParagraph with **bold** text."
        result = markdown_to_html_node(markdown)
        expected = ParentNode("div", [
            LeafNode("h1", "Header"),
            ParentNode("p", [
                LeafNode(None, "Paragraph with "),
                LeafNode("b", "bold"),
                LeafNode(None, " text.")
            ])
        ])
        self.assertEqual(result, expected)

    def test_list_to_html_node(self):
        text = "- item1\n- item2\n- item3"
        result = list_to_html_node(text, BlockType.UNORDERED_LIST)
        expected = ParentNode("ul", [
            ParentNode("li", [LeafNode(None, "item1")]),
            ParentNode("li", [LeafNode(None, "item2")]),
            ParentNode("li", [LeafNode(None, "item3")])
        ])

        self.assertEqual(result, expected)

        text = "1. item1\n2. item2\n3. item3"
        result = list_to_html_node(text, BlockType.ORDERED_LIST)
        expected = ParentNode("ol", [
            ParentNode("li", [LeafNode(None, "item1")]),
            ParentNode("li", [LeafNode(None, "item2")]),
            ParentNode("li", [LeafNode(None, "item3")])
        ])
        self.assertEqual(result, expected)

    def test_quote_to_html_node(self):
        text = "> This is a quote"
        result = quote_to_html_node(text)
        expected = LeafNode("blockquote", "This is a quote")
        self.assertEqual(result, expected)

    def test_code_to_html_node(self):
        text = "```\ncode block\n```"
        result = code_to_html_node(text)
        expected = ParentNode("pre", [LeafNode("code", ["code block"])])
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()