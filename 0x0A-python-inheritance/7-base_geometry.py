#!/usr/bin/python3
"""Contains definition of an empty cls BaseGeometry."""


class BaseGeometry:
    """The base geometry class representation."""

    def area(self):
        """Method not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value parameter to ensure its an int
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
