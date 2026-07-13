#!/usr/bin/python3
"""Module that defines the MyList class."""


class MyList(list):
    """A list class that can also print itself in sorted order."""

    def print_sorted(self):
        """Print the list in ascending sorted order."""
        print(sorted(self))
