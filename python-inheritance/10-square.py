#!/usr/bin/python3
"""Module that defines the Square class."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square, based on the Rectangle class."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the square's sides.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
