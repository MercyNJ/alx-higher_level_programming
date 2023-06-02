#!/usr/bin/python3
"""A function that prints a square"""


def print_square(size):
    """Print a square with the # char.

    Args:
        size (int): The len of the square.

    Raises:
        TypeError: if size is not an int.
        ValueError: if size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
