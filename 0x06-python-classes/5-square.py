#!/usr/bin/python3

"""
File: 5-square.py
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

    def my_print(self):
        """
        This method prints the square with the character '#' based on the size.
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end="")
                print("")
