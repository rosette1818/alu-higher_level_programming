#!/usr/bin/python3
"""Module that defines the from_json_string function."""
import json


def from_json_string(my_str):
    """Return a Python data structure from a JSON string.

    Args:
        my_str (str): The JSON string to convert.

    Returns:
        The Python data structure represented by my_str.
    """
    return json.loads(my_str)
