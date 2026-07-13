#!/usr/bin/python3
"""Module that defines the MyInt class."""


class MyInt(int):
    """A rebel integer class with == and != operators inverted."""

    def __eq__(self, other):
        """Return True if not equal, mimicking an inverted == operator."""
        return int(self) != int(other)

    def __ne__(self, other):
        """Return True if equal, mimicking an inverted != operator."""
        return int(self) == int(other)
