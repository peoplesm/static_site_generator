import re


def extract_markdown_images(text):

    # We exclude [] with '[^\[\]]' so if there are [] inside of the main [] we know there is accidental overlapping. [foo [] bar] is no good.
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def extract_markdown_links(text):

    # (?<!!) means it will discard the string if it matches '!' before the main expression. The '!' makes the markdown string an image vs. link.
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
