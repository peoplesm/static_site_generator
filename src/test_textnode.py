import unittest

from textnode import TextNode, TextType


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


if __name__ == "__main__":
    unittest.main()
