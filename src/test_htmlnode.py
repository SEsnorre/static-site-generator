import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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
        
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )

    
        
if __name__ == "__main__":
    unittest.main()