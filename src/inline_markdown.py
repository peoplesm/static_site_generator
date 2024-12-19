import re
from textnode import TextType, TextNode


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        split_nodes = []
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_text = old_node.text.split(delimiter)
        if len(split_text) % 2 == 0:
            raise ValueError("Need a closing delimiter")
        for text in split_text:
            if text == "":
                continue
            if split_text.index(text) % 2 == 0:
                split_nodes.append(TextNode(text, TextType.TEXT))
            else:
                split_nodes.append(TextNode(text, text_type))
        new_nodes.extend(split_nodes)

    return new_nodes


def extract_markdown_images(text):

    # We exclude [] with '[^\[\]]' so if there are [] inside of the main [] we know there is accidental overlapping. [foo [] bar] is no good.
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def extract_markdown_links(text):

    # (?<!!) means it will discard the string if it matches '!' before the main expression. The '!' makes the markdown string an image vs. link.
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
