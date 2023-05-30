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
    @property
    def size(self):
        """Get size of square"""

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Square area calculation
        Return: The square area
        """

        return (self.__size ** 2)

    def my_print(self):
        """print square using # """

        if self.__size == 0:
            print()

        for element in range(self.__size):
            print("#" * self.__size)
