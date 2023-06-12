#!/usr/bin/python3
"""Function checks if given object is an istance of class"""


def is_same_class(obj, a_class):
    """Checks if obj is exactly an instance of a given class

    Args:
        obj (any): The object to be checked
        a_class (type): Class to compare the type of obj to.

    Returns:
        True - if obj is exactly an instance of a_class.
        False - if not.
    """
    if type(obj) == a_class:
        return True
    return False
