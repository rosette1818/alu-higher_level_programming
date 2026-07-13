#!/usr/bin/python3
"""Module that defines the Student class."""


class Student:
    """Represent a student with a first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the Student instance.

        Args:
            attrs (list): Optional list of attribute names to include.
                If not a list of strings, all attributes are included.

        Returns:
            dict: A filtered or full dictionary of the instance's
                attributes.
        """
        result = {}
        if type(attrs) == list:
            for key in attrs:
                if type(key) == str and hasattr(self, key):
                    result[key] = getattr(self, key)
            return result
        return self.__dict__
