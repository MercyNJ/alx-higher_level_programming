#!/usr/bin/python3
"""Defines a module that inherits from list"""

class MyList(list):
    """A class that implements a sorted list"""

    def print_sorted(self):
        """Prints a sorted list in ascending order"""
        print(sorted(self))
