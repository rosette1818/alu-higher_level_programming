#!/usr/bin/python3
"""Module that defines the LockedClass class."""


class LockedClass:
    """Prevent the dynamic creation of new instance attributes,
    except for the attribute first_name.
    """

    __slots__ = ['first_name']
