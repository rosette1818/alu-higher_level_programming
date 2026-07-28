#!/usr/bin/python3
"""Module that prints text with new lines after ., ? and :
"""


def text_indentation(text):
    """Print text, adding two new lines after each ., ? and :

    Args:
        text: string to print.

    Raises:
        TypeError: if text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    built = ""
    for char in text:
        built += char
        if char in ".?:":
            built += "\n\n"

    lines = [line.strip() for line in built.split("\n")]
    print("\n".join(lines).strip("\n"))
