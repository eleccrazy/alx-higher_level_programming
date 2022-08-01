#!/usr/bin/python3

"""
File: 2-is_same_class.py
Desc: This module contains a single function.
Author: Gizachew Bayness (Elec Crazy)
Date Created: Aug 1 2022
"""


def is_same_class(obj, a_class):
    """
    This function checks  if the object is exactly an
    instance of the specified class
    """

    if type(obj) == a_class:
        return True
    return False
