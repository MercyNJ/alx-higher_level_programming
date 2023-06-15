#!/usr/bin/python3
"""This module contains rectangle class"""

from models.base import Base

class Rectangle(Base):
    """Rectangle class inheriting from base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing a rectangle instance"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter method for width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width's attribue setter method"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Height attribute's getter method"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height attributes's setter method"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """X-Coordinate attribute's getter method"""
        return self.__x

    @x.setter
    def x(self, value):
        """x-coordinate attribute's setter method"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """y-coordinate attribute's getter method"""
        return self.__y

    @y.setter
    def y(self, value):
        """y-coordinate attributes' getter method"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
       """Computes and returns rectangle's area"""
       return (self.__width * self.__height)

    def display(self):
        """Uses # char to print rectangle instance"""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.width)

    def __str__(self):
        """Returns string representation of rectangle."""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """Assigns key/value args to rectangle's attributes"""
        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dict representation of rectangle instance"""
        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }
