#!/usr/bin/python3
"""Module that defines the add_attribute function."""


def add_attribute(obj, name, value):
    """Add a new attribute to an object if possible.

    Args:
        obj: The object to add the attribute to.
        name (str): The name of the new attribute.
        value: The value to assign to the new attribute.

    Raises:
        TypeError: If the object doesn't support new attributes.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
