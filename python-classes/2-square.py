#!/usr/bin/python3
"""Module that defines a Square with validation."""


class Square:
    """Defines a square by size with type and value validation."""

    def __init__(self, size=0):
        """
        Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
