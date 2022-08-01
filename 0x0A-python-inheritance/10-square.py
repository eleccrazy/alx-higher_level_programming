#!/usr/bin/python3

"""
File: 10-square.py
Desc: This modlue contains a single class defination.
Author: Gizachew Bayness (Elec Crazy)
Date Created: Aug 1 2022
"""
R = __import__('9-rectangle').Rectangle


class Square(R):
    """
    This class inheretes from Rectangle class.
    """
    def __init__(self, size):
        """
        This function initializes the size attribute.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
