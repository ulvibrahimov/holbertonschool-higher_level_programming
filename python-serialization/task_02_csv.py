#!/usr/bin/python3
"""
Module that converts a CSV file to a JSON file.
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Reads data from a CSV file and converts it to a JSON format.

    Args:
        csv_filename (str): The name of the input CSV file.

    Returns:
        bool: True if conversion was successful, False otherwise.
    """
    try:
        # Read the CSV file
        with open(csv_filename, 'r', encoding='utf-8') as csvf:
            csv_reader = csv.DictReader(csvf)
            # Convert the reader object into a list of dictionaries
            data = list(csv_reader)

        # Write the serialized data to a JSON file
        with open('data.json', 'w', encoding='utf-8') as jsonf:
            json.dump(data, jsonf)

        return True

    except FileNotFoundError:
        return False
    except Exception:
        return False
