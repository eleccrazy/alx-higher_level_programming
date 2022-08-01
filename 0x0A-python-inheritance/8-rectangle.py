#!/usr/bin/python3

"""
File: 8-rectangle.py
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
