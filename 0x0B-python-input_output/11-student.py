#!/usr/bin/python3
"""Module contains definition of a student's class"""

class Student:
    """Student's representation."""

    def __init__(self, first_name, last_name, age):
        """Constructor for a new student creation"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves dict repr of a student instance.
           If attrs is list of strings, only attrs in
           list are included.
        """

        if attrs is not None and isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""
        for key, value in json.items():
            setattr(self, key, value)
