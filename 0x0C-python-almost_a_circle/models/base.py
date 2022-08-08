#!/usr/bin/python3

"""
File: base.py
Desc: This module contains a single class calld Base.
Author: Gizachew Bayness (Elec Crazy)
Date Created: Aug 6 2022
"""
from json import dumps as ds
from json import loads as ls


class Base:
    """
    The base for all other classes in this project.
    """
    __nb_objects = 0

    def __init__(self, id=0):
        """
        This function instantantiates all the attributes.
        """
        if id == 0 or id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        This method  returns the JSON string representation
        of list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        return ds(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        This method writes the JSON string representation of
        list_objs to a file
        """
        with open(cls.__name__+".json", "w", encoding="utf8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                ls = [obj.to_dictionary() for obj in list_objs]
                f.write(Base.to_json_string(ls))

    @staticmethod
    def from_json_string(json_string):
        """
        This method returns the list of the JSON string representation
        json_string
        """
        if json_string is None:
            return []
        else:
            return ls(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        This method returns an instance with all attributes already set
        """
        if dictionary and dictionary != {}:
            name = cls.__name__
            if name == "Rectangle":
                r = cls(1, 2)
                r.update(**dictionary)
                return r
            else:
                s = cls(1)
                s.update(**dictionary)
                return s

    @classmethod
    def load_from_file(cls):
        """
        This method returns a list of instances
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
