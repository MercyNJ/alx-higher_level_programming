#!/usr/bin/python3
"""a class inheriting from BseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle geometry representation"""

    def __init__(self, width, height):
        """Initialization of a new rectangle"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns calculated area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns the string repr of rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
