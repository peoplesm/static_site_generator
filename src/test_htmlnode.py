import unittest
from htmlnode import *


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

    # LeafNode tests
    def test_leaf_constructor(self):
        node_no_props = LeafNode("p", "This is a paragraph of text.")
        node_with_props = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node_no_props.to_html(), "<p>This is a paragraph of text.</p>")
        self.assertEqual(
            node_with_props.to_html(), '<a href="https://www.google.com">Click me!</a>'
        )

    def test_to_html_value_error(self):
        node = LeafNode("p")
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_no_tag(self):
        node = LeafNode(tag=None, value="This is text.")
        self.assertEqual(node.to_html(), node.value)
