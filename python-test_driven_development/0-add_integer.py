#!/usr/bin/python3
"""Module for adding two integers.
"""


def add_integer(a, b=98):
    """Adds two integers or floats (casted to int).

    Args:
        a: first number, int or float
        b: second number, int or float, default 98

    Returns:
        int: sum of a and b

    Raises:
        TypeError: if a or b is not an int or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
