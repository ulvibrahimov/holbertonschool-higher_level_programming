#!/usr/bin/python3
"""Module that defines a Square with a size."""


class Square:
    """Defines a square by its size."""

    def __init__(self, size):
        """
        Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size
