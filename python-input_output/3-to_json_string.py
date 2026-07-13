#!/usr/bin/python3
"""Module that defines the to_json_string function."""
import json


def to_json_string(my_obj):
    """Return the JSON string representation of an object.

    Args:
        my_obj: The object to convert to a JSON string.

    Returns:
        str: The JSON string representation of my_obj.
    """
    return json.dumps(my_obj)
