import unittest
from inline_markdown import *

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_code_block(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_inlinecode_nodes([node])
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)
        
    def test_invalid_markdown(self):
        node = TextNode("this is an invalid `code block word", TextType.TEXT)
        self.assertRaises(Exception, split_inlinecode_nodes, node)
    
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
        
    def test_multiple_Textnodes(self):
        node = TextNode("This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",TextType.TEXT)
        node2 = TextNode("This is text with another image ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT)
        new_nodes = split_nodes_image([node, node2])
        expected = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.IMAGE, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode(
                "to youtube", TextType.IMAGE, "https://www.youtube.com/@bootdotdev"
            ),
            TextNode("This is text with another image ", TextType.TEXT),
            TextNode("to boot dev", TextType.IMAGE, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode(
                "to youtube", TextType.IMAGE, "https://www.youtube.com/@bootdotdev"
            ),
        ]
        self.assertEqual(new_nodes,expected)
        
    def test_empty_node_list(self):
        new_nodes = split_nodes_image([])
        expected = []
        self.assertEqual(new_nodes, expected)

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


class TestTextToTextnodes(unittest.TestCase):
    def test_line_with_all_elements(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        result = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual(result,expected)
        
    def test_only_bold_text(self):
        text = "**this is only bold**"
        result = text_to_textnodes(text)
        expected = [
            TextNode("this is only bold", TextType.BOLD)
        ]
        self.assertEqual(result, expected)
        
    def test_only_one_image(self):
        text = "![image](https://www.some.url)"
        result = text_to_textnodes(text)
        expected = [
            TextNode("image", TextType.IMAGE, "https://www.some.url")
        ]
        self.assertEqual(result, expected)
        
    def test_empty_text(self):
        text = ""
        result = text_to_textnodes(text)
        expected = []
        self.assertEqual(result, expected)
        
    def test_invalid_markdown(self):
        text = "this should be **bold"
        text2 = "this is **bold** and this *italic"
        self.assertRaises(Exception, text_to_textnodes, text)
        self.assertRaises(Exception, text_to_textnodes, text2)
        

if __name__ == "__main__":
    unittest.main()