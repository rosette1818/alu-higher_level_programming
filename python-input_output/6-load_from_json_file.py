#!/usr/bin/python3
"""Module that defines the load_from_json_file function."""
import json


def load_from_json_file(filename):
    """Create an object from the JSON content of a file.

    Args:
        filename (str): The name of the JSON file to read.

    Returns:
        The Python data structure represented by the file's content.
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
