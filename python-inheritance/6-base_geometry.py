#!/usr/bin/python3
"""Module that defines the BaseGeometry class."""


class BaseGeometry:
    """Base class for future geometry classes."""

    def area(self):
        """Raise an exception since area() is not implemented."""
        raise Exception("area() is not implemented")
