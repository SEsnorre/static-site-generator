import unittest
from htmlnode import HTMLNode,LeafNode

class TestHTMLNode(unittest.TestCase):
    
    def test_props_to_html(self):
        props1 = {"href": "https://boot.dev"}
        props2 = {"href": "https://boot.dev", "target": "_blank"}

        node = HTMLNode(props=props1)
        node2 = HTMLNode(props=props2)
        
        self.assertEqual(node.props_to_html(), ' href="https://boot.dev"')
        self.assertEqual(node2.props_to_html(), ' href="https://boot.dev" target="_blank"')
        
class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        leaf_no_value = LeafNode("p", None) 
        leaf_no_tag = LeafNode(None, "This is a paragraph of text.")
        leaf1 = LeafNode("p", "This is a paragraph of text.")
        leaf2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        
        self.assertRaises(ValueError, leaf_no_value.to_html)
        self.assertEqual(leaf_no_tag.to_html(), "This is a paragraph of text.")
        self.assertEqual(leaf1.to_html(), "<p>This is a paragraph of text.</p>")
        self.assertEqual(leaf2.to_html(), '<a href="https://www.google.com">Click me!</a>')
        
if __name__ == "__main__":
    unittest.main()