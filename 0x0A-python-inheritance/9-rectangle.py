#!/usr/bin/python3

"""
File: 9-rectangle.py
Desc: This module contains a single class defination.
Author: Gizachew Bayness (Elec Crazy).
Date Created: Aug 1 2022
"""
B = __import__('7-base_geometry').BaseGeometry


class Rectangle(B):
    """
    This class inherits from BaseGeometry super class.
    """

    def __init__(self, width, height):
        """
        This function makes Instantiation of width and height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        This function computes the area of the rectangle.
        """
        return self.__height * self.__width

    def __str__(self):
        """
        The string representation of the instances of the class
        Rectangle with magic method __str__().
        """

        return ("[" + str(self.__class__.__name__) + "] " +
                str(self.__width) + "/" + str(self.__height))
