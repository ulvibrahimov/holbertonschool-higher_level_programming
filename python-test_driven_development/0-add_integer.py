#!/usr/bin/python3
"""
This module provides a function to add two integers.
It handles basic integer addition and casting from floats.
"""


def add_integer(a, b=98):
    """
    Adds two integers.
    
    Args:
        a: First number (int or float).
        b: Second number (int or float), defaults to 98.
        
    Returns:
        The addition of a and b as an integer.
        
    Raises:
        TypeError: If a or b is neither an integer nor a float.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
        
    return int(a) + int(b)
