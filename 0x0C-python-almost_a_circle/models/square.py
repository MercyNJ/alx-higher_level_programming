#!/usr/bin/python3
"""A module containing the class Square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization of a square instance"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Size attribute's getter method"""
        return self.width

    @size.setter
    def size(self, value):
        """Size attribute's setter method"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """Return str representation of square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Assigns attributes based on arguments"""
        attributes = ["id", "size", "x", "y"]
        if args:
            for i in range(len(args)):
                if i < len(attributes):
                    setattr(self, attributes[i], args[i])
                else:
                    raise IndexError("List index out of range")
        else:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns dict representation of square"""
        return ({"id": self.id, "size": self.size, "x": self.x, "y":self.y})


