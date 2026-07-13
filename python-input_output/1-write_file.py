#!/usr/bin/python3
"""Module that defines the write_file function."""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file and return chars written.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to write.

    Returns:
        int: The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
