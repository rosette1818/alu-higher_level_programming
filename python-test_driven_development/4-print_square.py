#!/usr/bin/python3
"""Module that prints a square using the # character.
"""


def print_square(size):
    """Print a square of side length size, using the # character.

    Args:
        size: integer, the length of the square's side.

    Raises:
        TypeError: if size is not an integer.
        ValueError: if size is less than 0.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
