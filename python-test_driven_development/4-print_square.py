#!/usr/bin/python3
"""Module that prints a square using the # character.
"""


def print_square(size):
    """Prints a square of size x size using the # character.

    Args:
        size: int, size length of the square

    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than 0
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
