#!/usr/bin/python3
"""
This module provides a function that formats text by adding 2 newlines
after specific punctuation marks (., ?, and :).
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':'.
    Removes leading and trailing spaces from each printed line.

    Args:
        text: The string to be formatted.

    Raises:
        TypeError: If text is not a string.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    # We copy the text, then process it one punctuation mark at a time
    s = text[:]
    for d in ".?:":
        # Split the text by the current punctuation mark
        list_text = s.split(d)
        s = ""
        for i, text_part in enumerate(list_text):
            # Strip ONLY spaces from the edges, leaving newlines intact
            text_part = text_part.strip(" ")
            if i == len(list_text) - 1:
                s += text_part
            else:
                s += text_part + d + "\n\n"

    print(s, end="")
