#!/usr/bin/python3

"""
File: rectangle.py
Desc: This module contains a class called Rectangle that
      inherits from the Base class in the base.py module.
Author: Gizachew Bayness (Elec Crazy)
Date Created: Aug 6 2022
"""
from models.base import Base as B


class Rectangle(B):
    """
    This Rectangle class represents a rectangle model, and
    inherits from the Base class model from models package.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        This method instatantiates instance attributes of
        rectangle.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        super().__init__(id)

    @property
    def width(self):
        """ Getter method for width attribute """
        return self.__width

    @width.setter
    def width(self, w):
        """ Setter method for width attribute """
        self.__width = w

    @property
    def height(self):
        """ Getter method for height attribute """
        return self.__height

    @height.setter
    def height(self, h):
        """ Setter method for height attribute """
        self.__height = h

    @property
    def x(self):
        """ Getter method for x attribute """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter method for x attribute """
        self.__x = value

    @property
    def y(self):
        """ Getter method for y attribute """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter method for y attribute """
        self.__y = value
