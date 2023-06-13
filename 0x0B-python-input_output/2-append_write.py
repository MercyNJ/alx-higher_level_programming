#!/usr/bin/python3
"""Module contains a function that appends text to file"""


def append_write(filename="", text=""):
    """Appends a str at the end of a UTF8 text file"""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
