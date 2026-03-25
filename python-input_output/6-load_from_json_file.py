#!/usr/bin/python3
"""Module that creates an Object from a JSON file."""
import json


def load_from_json_file(filename):
    """Creates a Python object from a given JSON file.

    Args:
        filename (str): The name of the file to read.

    Returns:
        object: The Python data structure from the JSON file.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
