from htmlnode import *
from textnode import *
from split_nodes_delimiter import split_nodes_delimiter


def main():
    node = TextNode("This is text with a *bold block*", TextType.TEXT)
    print(split_nodes_delimiter([node], "*", TextType.BOLD))


if __name__ == "__main__":
    main()
