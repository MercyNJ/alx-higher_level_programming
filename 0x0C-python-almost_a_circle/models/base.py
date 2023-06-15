#!/usr/bin/python3
"""This module defines a base class"""

class Base:
    """Represents the class that will serve as
       base for all other classes in this project
    
    Attributes:__nb_objects (int):
    Number of objects created from the class.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialiazing a base instance.

        Args:
            id (int): Instance ID, if none, unique one is assigned.

        Atrributes:
            id (int): Instance ID.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
