import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_url_is_none(self):
        node = TextNode("None url", TextType.BOLD)
        self.assertIsNone(node.url)

    def test_url_is_not_none(self):
        node = TextNode("Node has a url", TextType.TEXT, "https://www.boot.dev")
        self.assertIsNotNone(node.url)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_TextType(self):
        node = TextNode("TextType test node", TextType.ITALIC)
        self.assertEqual(node.text_type.value, "italic")


# Could have made the node2 by just calling the fxn on node and compared values that way. This way below requires me to import LeafNode from htmlnode.py and adding a __eq__ method to LeafNode class
class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text_node_to_html_node_text(self):
        node = TextNode("Words", TextType.TEXT)
        node2 = LeafNode(None, "Words", None)
        self.assertEqual(text_node_to_html_node(node), node2)

    def test_text_node_to_html_node_tag(self):
        node = TextNode("Words", TextType.BOLD)
        node2 = LeafNode("b", "Words", None)
        self.assertEqual(text_node_to_html_node(node), node2)

    def test_text_node_to_html_node_link(self):
        node = TextNode("Link", TextType.LINK, "https://www.boot.dev")
        node2 = LeafNode("a", "Link", {"href": "https://www.boot.dev"})
        self.assertEqual(text_node_to_html_node(node), node2)

    def test_text_node_to_html_node_img(self):
        node = TextNode("Alt Text", TextType.IMAGE, "./assets/pic.png")
        node2 = LeafNode("img", "", {"src": "./assets/pic.png", "alt": "Alt Text"})
        self.assertEqual(text_node_to_html_node(node), node2)


if __name__ == "__main__":
    unittest.main()
