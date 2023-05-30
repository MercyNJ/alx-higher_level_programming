#!/usr/bin/python3
""" Definining a square """


class Square:
    """A class square representation """

    def __init__(self, size=0):
        """Initialization of square class
        Args:
            size: Size of the square
        Raises:
            TypeError: if size is not int
            ValueError: if size less than zero
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """
        Square area calculation
        Return: The square area
        """

        return (self.__size ** 2)
