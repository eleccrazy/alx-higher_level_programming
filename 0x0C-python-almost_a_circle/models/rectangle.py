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
        if type(w) != int:
            raise TypeError("width must be an integer")
        if w <= 0:
            raise ValueError("width must be > 0")
        self.__width = w

    @property
    def height(self):
        """ Getter method for height attribute """
        return self.__height

    @height.setter
    def height(self, h):
        """ Setter method for height attribute """
        if type(h) != int:
            raise TypeError("height must be an integer")
        if h <= 0:
            raise ValueError("height must be > 0")
        self.__height = h

    @property
    def x(self):
        """ Getter method for x attribute """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter method for x attribute """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Getter method for y attribute """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter method for y attribute """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Computes and returns the area of the rectangle """
        return self.__height * self.__width
