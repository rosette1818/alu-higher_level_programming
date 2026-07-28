#!/usr/bin/python3
"""Module that prints text with 2 new lines after ., ? and :
"""


def text_indentation(text):
    """Prints a text, adding 2 new lines after each ., ? and :

    Args:
        text: str, the text to print

    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    marks = ".?:"
    line = ""
    for char in text:
        if char == " " and line == "":
            continue
        line += char
        if char in marks:
            print(line.strip())
            print("")
            line = ""
    if line.strip():
        print(line.strip())
