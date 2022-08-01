#!/usr/bin/python3

"""
File: 7-base_geometry.py
Desc: This module defines an empty class.
Author: Gizachew Bayness (Elec Crazy).
Date Created: Aug 1 2022
"""


class BaseGeometry:
    """
    A simple class defination.
    """

    def area(self):
        """
        A function that raises an Exception.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This function validates the value.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
