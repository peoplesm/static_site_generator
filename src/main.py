from htmlnode import *


def main():
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

    print(node.__repr__())


if __name__ == "__main__":
    main()
