#!/usr/bin/python3
"""Module that defines the class_to_json function."""


def class_to_json(obj):
    """Return the dictionary description of a simple object instance.

    Args:
        obj: An instance of a class with only serializable attributes
            (list, dict, str, int, bool).

    Returns:
        dict: A dictionary representation of obj's attributes.
    """
    return obj.__dict__
