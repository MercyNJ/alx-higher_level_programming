#!/usr/bin/python3
"""Module contains a function that prints a name"""


def say_my_name(first_name, last_name=""):
    """Output a name

    Args:
        first_name (str): The 1st name tobe  printed.
        last_name (str): The last name to be printed.

    Raises:
        TypeError: If either first_name/last_name are not strings.
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))

