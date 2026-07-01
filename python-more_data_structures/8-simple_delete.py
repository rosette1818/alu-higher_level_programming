#!/usr/bin/python3
"""Module that deletes a key in a dictionary."""
def simple_delete(a_dictionary, key=""):
    """Delete a key in a dictionary.
    Args:
        a_dictionary (dict): the dictionary.
        key (str): thekey to delete.
    Returns:
        dict: the dictionary with the key removed, if present.
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
