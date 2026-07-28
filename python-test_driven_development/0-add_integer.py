#!/usr/bin/python3
"""Module that adds two integers.
"""


def add_integer(a, b=98):
    """Add two integers or floats, casting floats to int first.

    Args:
        a: first number, must be an int or a float.
        b: second number, must be an int or a float, defaults to 98.

    Returns:
        The integer sum of a and b.

    Raises:
        TypeError: if a is not an integer or a float, or if b is not
            an integer or a float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
