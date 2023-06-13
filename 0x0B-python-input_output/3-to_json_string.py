#!/usr/bin/python3
"""Converts an object to its JSON representation"""
import json


def to_json_string(my_obj):
    """Returns obtained JSON representation of a str obj."""
    return json.dumps(my_obj)
