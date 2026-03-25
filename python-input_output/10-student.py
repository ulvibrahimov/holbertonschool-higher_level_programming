#!/usr/bin/python3
"""Module that defines a Student class with a filtered JSON serializer."""


class Student:
    """A class that represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance.

        If attrs is a list of strings, retrieves only those attributes.

        Args:
            attrs (list): Optional list of strings representing attributes.

        Returns:
            dict: The filtered or complete dictionary representation.
        """
        if type(attrs) is list and all(type(i) is str for i in attrs):
            return {k: self.__dict__[k] for k in attrs if k in self.__dict__}
        return self.__dict__
