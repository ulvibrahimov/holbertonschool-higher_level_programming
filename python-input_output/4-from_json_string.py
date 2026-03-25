#!/usr/bin/python3
"""Module that returns an object from a JSON string."""
import json


def from_json_string(my_str):
    """Returns an object represented by a JSON string.

    Args:
        my_str (str): The JSON string to deserialize.

    Returns:
        object: The Python data structure from the JSON string.
    """
    return json.loads(my_str)
