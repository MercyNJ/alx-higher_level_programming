#!/usr/bin/python3
"""Contains a function that reads a text file"""


def read_file(filename=""):
    """Print content of a UTF8 txt file to stdout"""
    with open(filename, encoding="utf-8") as f:
        while True:
            text = f.readline()
            if not text:
                break
            print(text, end='')
