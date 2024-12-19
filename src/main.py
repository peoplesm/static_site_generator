from htmlnode import *
from textnode import *
from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
)


def main():
    test = extract_markdown_images(
        "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
    )

    print(
        test,
        extract_markdown_images(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif"
        ),
    )


if __name__ == "__main__":
    main()
