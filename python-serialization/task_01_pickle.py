#!/usr/bin/python3
"""
Module for serializing and deserializing custom objects using pickle.
"""
import pickle


class CustomObject:
    """A custom class to demonstrate pickling."""

    def __init__(self, name, age, is_student):
        """Initializes a new CustomObject.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            is_student (bool): Whether the person is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Prints out the object's attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serializes the current instance and saves it to a file.

        Args:
            filename (str): The file to save the pickled object to.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Loads and returns an instance of CustomObject from a file.

        Args:
            filename (str): The file to load the pickled object from.

        Returns:
            CustomObject: The deserialized object, or None on failure.
        """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception:
            return None
