#!/usr/bin/python3
"""A class defining a rectangle"""


class Rectangle:
    """A class representation of  a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializing a rectangle object with optional width and height

        Args:
            width: Rectangle width
            height: Rectangle height

        Raises:
            TypeError: if size is not an int
            ValueError: if size is less than 0
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
