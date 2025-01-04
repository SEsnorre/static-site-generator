import unittest

from textnode import Textnode, TextType



class TestTextNode(unittest.TestCase):

    node = Textnode("This is a text node", TextType.BOLD)
    node2 = Textnode("This is a text node", TextType.BOLD, None)
    node3 = Textnode("This is another Node", TextType.BOLD)

    def test_eq(self):
        self.assertEqual(self.node, self.node2)
        
    def test_not_eq(self):
        self.assertNotEqual(self.node2, self.node3)
        self.assertNotEqual(self.node, self.node3)
    
    
        
if __name__ == "__main__":
    unittest.main()