#!/usr/bin/python3

"""
File: 0-lookup.py
Desc: This module conatins a single function called lookup.
Author: Gizachew Bayness (Elec Crazy).
Date Created: Aug 1 2022
"""


def lookup(obj):
    """
    This function returns the list of available attributes
    and methods of an object.
    """
    return (dir(obj))
