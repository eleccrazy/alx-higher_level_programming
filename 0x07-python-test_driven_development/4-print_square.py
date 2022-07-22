#!/usr/bin/python3

"""
File: 4-print_square.py
Desc: This module supplies one function called print_square.
Author: Gizachew Bayness (Elec Crazy)
Date Created: Jul 22 2022
"""


def print_square(size):
    """
    This function prints a square with the character '#'
    Depending on the size argument.
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for rows in range(size):
        [print("#", end="") for rows in range(size)]
        print("")
