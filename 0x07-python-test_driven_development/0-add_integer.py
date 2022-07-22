#!/usr/bin/python3
"""
File: 0-add_integer.py
Desc: This module contains defination of a single function.
Author: Gizachew Bayness (Elec Crazy)
Date Created: Jul 21 2022
"""


def add_integer(a, b=98):
    """
    This function computes the addition of two integer numbers
    """
    if type(a) not in [float, int]:
        raise TypeError("a must be an integer")
    if type(b) not in [float, int]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
