#!/usr/bin/python3
"""Module contains definition of a student's class"""

class Student:
    """Student's representation."""

    def __init__(self, first_name, last_name, age):
        """Constructor for a new student creation"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves dict repr of a student instance"""
        return self.__dict__
