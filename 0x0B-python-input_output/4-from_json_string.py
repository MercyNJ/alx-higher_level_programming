#!/usr/bin/python3
"""Module contains a function converting JSON-to-obj."""
import json


def from_json_string(my_str):
    """Returns Python obj's representation of a JSON str."""
    return json.loads(my_str)
