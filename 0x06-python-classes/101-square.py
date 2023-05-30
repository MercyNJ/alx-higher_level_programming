class Square:
    """Class square definition"""

    def __init__(self, size=0, position=(0, 0)):
        """Creation of a Square
        Args:
            size: Square's side length
            position: square coordinates
        """
        self.size = size
        self.position = position

    def __str__(self):
        return self.pos_print()[:-1]

    @property
    def size(self):
        """The size of Square
        Raises:
            TypeError: if size is not an int
            ValueError: if size is less than zero
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """Square coordinates
        Raises:
            TypeError: if value != a tuple of 2 ints
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set square's position
        Args: A tuple of 2 positive integers
        Raises:
            TypeError: if value is not a tuple or any int
        """
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([n for n in value if isinstance(n, int) and n >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Get the area of a Square
        Returns: The size squared
        """
        return self.__size * self.__size

    def pos_print(self):
        """Output the position in spaces"""
        pos = ""
        if self.size == 0:
            return "\n"
        for e in range(self.position[1]):
            pos += "\n"
        for e in range(self.size):
            for i in range(self.position[0]):
                pos += " "
            for j in range(self.size):
                pos += "#"
            pos += "\n"
        return pos

    def my_print(self):
        """Print square in position"""
        print(self.pos_print(), end='')
