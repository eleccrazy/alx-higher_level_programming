#!/usr/bin/python3

"""
File: 10-student.py
Desc: This module deals with classes and json
Author: Gizachew Bayness (Elec Crazy)
Date Created: Aug 2 2022
"""


class Student():
    """
    A simple stundent class.
    """
    def __init__(self, first_name, last_name, age):
        """
        This function initializes the object parameters.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        This function retrieves a dictionary representation
        of a Student instance
        """
        if type(attrs) == list and all(type(i) == str for i in attrs):
            return ({key: getattr(self, key)
                    for key in attrs if hasattr(self, key)})
        return self.__dict__
