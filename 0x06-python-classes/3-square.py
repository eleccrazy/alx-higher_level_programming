#!/usr/bin/python3

"""
File: 3-square.py
Desc: This module contains a single class defination called Size.
Author: Gizachew Bayness (Elec Crazy)
Date Created: Jul 19 2022
"""


class Square():
    """
    This class contains a defination of a single private object attribute
    called size, and checks the attribute if it is integer and positive.
    """
    def __init__(self, size=0):
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """
        This method computes and returns the square based on the size.
        """
        return (self.__size ** 2)
