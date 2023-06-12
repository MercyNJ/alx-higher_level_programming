#!/usr/bin/python3
"""Contains class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square rectangle representation"""

    def __init__(self, size):
        """Constructor for a new square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Returns description of square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
