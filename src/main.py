from htmlnode import *


def main():

    test = HTMLNode(
        "a", "google", props={"href": "https://www.google.com", "target": "_blank"}
    )

    print(test)


if __name__ == "__main__":
    main()
