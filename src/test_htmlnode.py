import unittest
from htmlnode import LeafNode, ParentNode, HTMLNode


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
    def test_leaf_to_html(self):
        node_no_props = LeafNode("p", "This is a paragraph of text.")
        node_with_props = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node_no_props.to_html(), "<p>This is a paragraph of text.</p>")
        self.assertEqual(
            node_with_props.to_html(), '<a href="https://www.google.com">Click me!</a>'
        )

    def test_to_html_value_error(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_no_tag(self):
        node = LeafNode(tag=None, value="This is text.")
        self.assertEqual(node.to_html(), node.value)

    def test_repr_LeafNode(self):
        node = LeafNode(
            "a", "google", props={"href": "https://www.google.com", "target": "_blank"}
        )
        self.assertEqual(
            node.__repr__(),
            "LeafNode(a, google, {'href': 'https://www.google.com', 'target': '_blank'})",
        )

    # ParentNode Tests
    def test_parent_to_html(self):
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

    def test_parent_to_html_with_nested_parent(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                ParentNode(
                    "p",
                    [
                        LeafNode("i", "nested"),
                        LeafNode("b", "parent with children"),
                    ],
                ),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b><p><i>nested</i><b>parent with children</b></p>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_no_children_value_error(self):
        node = ParentNode("p", None, None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_no_tag_value_error(self):
        node = ParentNode(
            None,
            [
                LeafNode("b", "GNX"),
            ],
            None,
        )
        with self.assertRaises(ValueError):
            node.to_html()

    def test_repr_ParentNode(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
            props={"class": "introduction"},
        )

        self.assertEqual(
            node.__repr__(),
            "ParentNode(p, [LeafNode(b, Bold text, None), LeafNode(None, Normal text, None), LeafNode(i, italic text, None), LeafNode(None, Normal text, None)], {'class': 'introduction'})",
        )

    def test_to_html_parent_with_props(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
            props={"class": "introduction"},
        )

        self.assertEqual(
            node.to_html(),
            '<p class="introduction"><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>',
        )

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )


if __name__ == "__main__":
    unittest.main()
