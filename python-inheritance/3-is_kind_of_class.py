#!/usr/bin/python3
"""This module contains the function is_kind_of_class."""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance or inherited instance of a class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance or inherited instance of a_class,
        False otherwise.
    """
    return isinstance(obj, a_class)
