import unittest
from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_links,
    extract_markdown_images,
)
from textnode import TextNode, TextType


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_value_error(self):
        node = TextNode("This is text with a `code block` `word", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "`", TextType.CODE)

    def test_bold(self):
        node = TextNode("I want **BOLD** text", TextType.TEXT)
        delimited_list = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("I want ", TextType.TEXT),
                TextNode("BOLD", TextType.BOLD),
                TextNode(" text", TextType.TEXT),
            ],
            delimited_list,
        )

    def test_double_bold(self):
        node = TextNode("I want **BOLD** text **twice**", TextType.TEXT)
        delimited_list = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("I want ", TextType.TEXT),
                TextNode("BOLD", TextType.BOLD),
                TextNode(" text ", TextType.TEXT),
                TextNode("twice", TextType.BOLD),
            ],
            delimited_list,
        )

    def test_multi_bold_words(self):
        node = TextNode("I want **BOLD words** text **twice**", TextType.TEXT)
        delimited_list = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("I want ", TextType.TEXT),
                TextNode("BOLD words", TextType.BOLD),
                TextNode(" text ", TextType.TEXT),
                TextNode("twice", TextType.BOLD),
            ],
            delimited_list,
        )

    def test_italic(self):
        node = TextNode("I want *Italic* word", TextType.TEXT)
        delimited_list = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("I want ", TextType.TEXT),
                TextNode("Italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            delimited_list,
        )

    def test_code(self):
        node = TextNode("I want `Code` word", TextType.TEXT)
        delimited_list = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("I want ", TextType.TEXT),
                TextNode("Code", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            delimited_list,
        )

    def test_bold_and_italic(self):
        node = TextNode("**bold** and *italic*", TextType.TEXT)
        delimited_list = split_nodes_delimiter([node], "**", TextType.BOLD)
        delimited_list = split_nodes_delimiter(delimited_list, "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            delimited_list,
        )


class TestExtractMarkdownImages(unittest.TestCase):
    def test_one_image(self):
        extracted_list = extract_markdown_images(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
        )
        self.assertListEqual(
            [("rick roll", "https://i.imgur.com/aKaOqIh.gif")],
            extracted_list,
        )

    def test_two_images(self):
        extracted_list = extract_markdown_images(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        )
        self.assertListEqual(
            [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
            ],
            extracted_list,
        )

    def test_link_instead_image(self):
        extracted_list = extract_markdown_images(
            "This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif)"
        )
        self.assertListEqual([], extracted_list)


class TestExtractMarkdownLinks(unittest.TestCase):
    def test_one_link(self):
        extracted_list = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev)"
        )
        self.assertListEqual(
            [("to boot dev", "https://www.boot.dev")],
            extracted_list,
        )

    def test_two_links(self):
        extracted_list = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual(
            [
                ("to boot dev", "https://www.boot.dev"),
                ("to youtube", "https://www.youtube.com/@bootdotdev"),
            ],
            extracted_list,
        )

    def test_image_instead_link(self):
        extracted_list = extract_markdown_links(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
        )
        self.assertListEqual([], extracted_list)
