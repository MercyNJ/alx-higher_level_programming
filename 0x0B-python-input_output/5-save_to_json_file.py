#!/usr/bin/python3
"""Module contains function to write object to text file"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an obj to a txt file using JSON representation."""
    with open(filename, "w") as file:
        json.dump(my_obj, file)
