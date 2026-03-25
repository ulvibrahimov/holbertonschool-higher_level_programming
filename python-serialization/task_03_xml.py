#!/usr/bin/python3
"""
Module for serializing and deserializing dictionaries using XML.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary into an XML file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The name of the output XML file.
    """
    # Create the root element
    root = ET.Element("data")

    # Add child elements for each dictionary item
    for key, val in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(val)

    # Write the tree to the file
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8')


def deserialize_from_xml(filename):
    """
    Deserializes an XML file into a Python dictionary.

    Args:
        filename (str): The name of the input XML file.

    Returns:
        dict: The reconstructed dictionary.
    """
    try:
        # Parse the XML file
        tree = ET.parse(filename)
        root = tree.getroot()

        # Reconstruct the dictionary using dictionary comprehension
        return {child.tag: child.text for child in root}
    except Exception:
        return None
