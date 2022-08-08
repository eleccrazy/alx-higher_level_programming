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

    def display(self):
        """
        prints in stdout the Rectangle instance with the
        character #
        """
        for y in range(self.__y):
            print()
        for h in range(self.__height):
            [print(' ', end='') for x in range(self.__x)]
            [print('#', end='') for w in range(self.__width)]
            print()

    def __str__(self):
        """
        Returns the string representation of the Rectangle object.
        """
        string = "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.__x, self.__y, self.__width, self.__height)
        return string

    def update(self, *args, **kwargs):
        """
        This method assigns an argument to each attribute
        """
        if args:
            length = len(args)
            self.id = args[0]
            if length > 1:
                self.width = args[1]
                if length > 2:
                    self.height = args[2]
                    if length > 3:
                        self.x = args[3]
                        if length > 4:
                            self.y = args[4]
        elif kwargs:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'y':
                    self.y = value
                elif key == 'x':
                    self.x = value
                elif key == 'width':
                    self.width = value
                elif key == 'height':
                    self.height = value
                else:
                    pass

    def to_dictionary(self):
        """
        This method returns the dictionary representaiton
        of a rectangle.
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
