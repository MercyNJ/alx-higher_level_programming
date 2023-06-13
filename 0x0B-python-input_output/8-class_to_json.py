#!/usr/bin/python3
"""Contains a function that returns dict representation"""


def class_to_json(obj):
    """Gives the dictionary description of a simple data structure."""
    return obj.__dict__
