#!/usr/bin/python3
"""Module that contains a function that appends to a text file."""


def append_write(filename="", text=""):
    """Appends a string to the end of a text file (UTF8).

    Returns the number of characters added.

    Args:
        filename (str): The name of the file.
        text (str): The text to append.

    Returns:
        int: The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
