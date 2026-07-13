#!/usr/bin/python3
"""Module that defines the read_file function."""


def read_file(filename=""):
    """Read a UTF8 text file and print its content to stdout.

    Args:
        filename (str): The name of the file to read.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
