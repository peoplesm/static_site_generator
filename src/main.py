from htmlnode import *


def main():
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

    print(node.to_html())


if __name__ == "__main__":
    main()
