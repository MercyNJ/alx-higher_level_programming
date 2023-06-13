#!/usr/bin/python3
"""Module contains function that writes to a file"""

def write_file(filename="", text=""):
    """Writes a str to a UTF8 encoded txt file"""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
