from htmlnode import *
from textnode import *


def main():
    node = TextNode("Hello", TextType.BOLD, None)

    print(text_node_to_html_node(node))


if __name__ == "__main__":
    main()
