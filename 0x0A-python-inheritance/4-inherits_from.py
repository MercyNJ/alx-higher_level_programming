#!/usr/bin/python3
"""checks if given obj is an instance of a class that
inherited from provided class or not
"""


def inherits_from(obj, a_class):
    """Returns: true if obj is an instance of a cls that inherited
     directly/indirectly from the specified class; Otherwise: False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
