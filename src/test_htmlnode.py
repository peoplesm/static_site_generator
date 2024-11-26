import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_default_is_none(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_props_to_html(self):
        node = HTMLNode(
            "a", "google", props={"href": "https://www.google.com", "target": "_blank"}
        )
        self.assertEqual(
            node.props_to_html(), ' href="https://www.google.com" target="_blank"'
        )

    def test_props_to_html_none(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

    def test_repr(self):
        node = HTMLNode(
            "a", "google", props={"href": "https://www.google.com", "target": "_blank"}
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(a, google, None, {'href': 'https://www.google.com', 'target': '_blank'})",
        )
