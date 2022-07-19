#!/usr/bin/python3

"""
File: 102-square.py
Desc: This module contains a single class defination called Size.
Author: Gizachew Bayness (Elec Crazy)
Date Created: Jul 19 2022
"""


class Square():
    """
    This square class contains some attribute definations, and method
    definations.
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """
        This method retrives the value of attribute size.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        This method sets the value of the attribute size.
        """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """
        This method computes and returns the square based on the size.
        """
        return (self.__size ** 2)

    def __eq__(self, other):
        """
        The equality representation of the class Square itself with
        the __eq__ magic method.
        """
        return self.__size == other.__size

    def __ne__(self, other):
        """
        The not equalto representation of the class Square itself
        with __ne__ magic method.
        """
        return self.__size != other.__size

    def __gt__(self, other):
        """
        The greater than representation of the class Square itself
        with __gt__ magic method.
        """
        return self.__size > other.__size

    def __ge__(self, other):
        """
        The greater or equalto representation of the class Square
        itself with __ge__ magic method.
        """
        return self.__size >= other.__size

    def __lt__(self, other):
        """
        The less than representation of the class Square itself
        with the __lt__ magic method.
        """
        return self.__size < other.__size

    def __le__(self, other):
        """
        The less than or equal to representation of the class Square
        itself with the __le__ magic method.
        """
        return self.__size <= other.__size
