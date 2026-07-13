#!/usr/bin/python3
"""Module that defines the is_same_class function."""


def is_same_class(obj, a_class):
    """Check if obj is exactly an instance of the specified class."""
    return type(obj) == a_class
