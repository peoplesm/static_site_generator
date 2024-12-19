import unittest
from extract_markdown import *


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
