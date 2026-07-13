#!/usr/bin/python3
"""Module that defines the LockedClass class."""


class LockedClass:
    """Prevent the dynamic creation of new instance attributes,
    except for the attribute first_name.
    """

    def __setattr__(self, name, value):
        """Set an attribute, only allowing first_name to be
        created dynamically.
        """
        if name != "first_name" and name not in self.__dict__:
            raise AttributeError("'{}' object has no attribute '{}'"
                                  .format(type(self).__name__, name))
        super().__setattr__(name, value)
