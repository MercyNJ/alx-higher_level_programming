#!/usr/bin/python3
"""Function checking if object is an
   instance of class or inherited class
"""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited instance of a class.
    Args:
        obj (any): The object of check.
        a_class (type): Class to compare the type of object to.

    Returns:
        True - If obj is an instance or inherited instance of a_class.
        False - if not
    """
    if isinstance(obj, a_class):
        return True
    return False
