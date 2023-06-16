#!/usr/bin/python3
"""This module defines a base class"""
import json
import csv

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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts & returns JSON str representation of list_dict"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes JSON representation of list of instances to a file"""
        filename = cls.__name__ + ".json"
        json_list = []
        if list_objs is not None:
            json_list = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w") as file:
            file.write(cls.to_json_string(json_list))

    @staticmethod
    def from_json_string(json_string):
        """Returns the deserialized list of dictionaries

        Args:
            json_string (str): JSON str - list of dicts

        Returns:
            list: List of dicts represented by JSON str.
        """

        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns a base instance with attributes set"""
        if not dictionary:
            raise ValueError("Cannot create instance")
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()

        dummy.update(**dictionary)
        return (dummy)

    @classmethod
    def load_from_file(cls):
        """Returns list of instances loaded from file"""
        filename = cls.__name__ + ".json"
        instances = []
        try:
            with open(filename, "r") as file:
                json_data = file.read()
                dictionaries = cls.from_json_string(json_data)
                for dictionary in dictionaries:
                    instance = cls.create(**dictionary)
                    instances.append(instance)
        except FileNotFoundError:
            return []

        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialization of list of instances to a csv file"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline='') as file:
            writer = csv.writer(file)

            if cls.__name__ == 'Rectangle':
                for obj in list_objs:
                    writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
            elif cls.__name__ == 'Square':
                for obj in list_objs:
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Returns list of instances deserialized from a CSV file"""
        filename = cls.__name__ + ".csv"
        instances = []

        try:
            with open(filename, 'r', newline="") as file:
                reader = csv.reader(file)
                for row in reader:
                    if cls.__name__ == "Rectangle" and len(row) == 5:
                        instance = cls(*map(int, row[1:]), id=int(row[0]))
                        instances.append(instance)
                    elif cls.__name__ == "Square" and len(row) == 4:
                        instance = cls(*map(int, row[1:]), id=int(row[0]))
                        instances.append(instance)
        except FileNotFoundError:
            return []
        return instances
