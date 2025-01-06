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
    
class TestExtractMarkdownImages(unittest.TestCase):
    def test_single_image(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
        expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif")]
        
        self.assertEqual(extract_markdown_images(text), expected)
        
        
    def test_for_two_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        
        self.assertEqual(extract_markdown_images(text), expected)
        
    def test_empty_string(self):
        text = ""
        expected = []
        self.assertEqual(extract_markdown_images(text), expected)
        
        
class TestExtractMarkdownLinks(unittest.TestCase):
    def test_single_link(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev)"
        expected = [("to boot dev", "https://www.boot.dev")]
        
        self.assertEqual(extract_markdown_links(text), expected)
        
    
    def test_for_two_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        expected = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        
        self.assertEqual(extract_markdown_links(text), expected)
        
    def test_empty_string(self):
        text = ""
        expected = []
        self.assertEqual(extract_markdown_links(text), expected)
        
        
class TestSplitNodesImages(unittest.TestCase):
    def test_single_Textnode(self):
        node = TextNode("This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",TextType.TEXT)
        new_nodes = split_nodes_image([node])
        expected = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.IMAGE, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode(
                "to youtube", TextType.IMAGE, "https://www.youtube.com/@bootdotdev"
            ),
        ]
        self.assertEqual(new_nodes,expected)
        

class TestSplitNodesLink(unittest.TestCase):
    def test_single_Textnode(self):
        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",TextType.TEXT)
        new_nodes = split_nodes_link([node])
        expected = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode(
                "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
            ),
        ]
        self.assertEqual(new_nodes,expected)

if __name__ == "__main__":
    unittest.main()