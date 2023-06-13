#!/usr/bin/python3
"""Module contains a function that creates an obj from a JSON file"""
import json


def load_from_json_file(filename):
    """Creates a Python obj from a JSON file."""
    with open(filename) as file:
        return json.load(file)
