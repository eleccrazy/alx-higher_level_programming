#!/usr/bin/python3

"""
File: 103-magic_class.py
Desc: This file contains the python code of reveresed version of
python byte code.
Author: Gizachew Bayness (Elec Crazy)
Date Created: Jul 19 2022

Reverse Engineering is really awesome!
"""
import math


class MagicClass():
    """
    MagicClass representation of python byte code given.
    """
    def __init__(self, radius=0):
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self):
        """
        This method computes the area of the given circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        This method computes the circumstance of the given circle.
        """
        return 2 * math.pi * self.__radius
