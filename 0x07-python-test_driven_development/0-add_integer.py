#!/usr/bin/python3
"""

This module contains a function that adds two numbers

"""


def add_integer(a, b=98):
    """ Function that adds two integer and/or float numbers

    Args:
        a: 1st num
        b: 2nd num

    Returns:
        The addition result of two nums

    Raises:
        TypeError: If either a or b are not int &/or float nums

    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
