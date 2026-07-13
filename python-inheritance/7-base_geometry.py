#!/usr/bin/python3
"""Module that defines the BaseGeometry class."""


class BaseGeometry:
    """Base class for future geometry classes."""

    def area(self):
        """Raise an exception since area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer.

        Args:
            name (str): The name of the attribute being validated.
            value: The value to validate.

        Raises:
            TypeError: If value is not an int.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
