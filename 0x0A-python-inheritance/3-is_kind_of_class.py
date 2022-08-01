#!/usr/bin/python3

"""
File: 3-is_kind_of_class.py
Desc: This file contains a single function defination
Author: Gizachew Bayness (Elec Crazy)
Date Created: Aug 1 2022
"""


def is_kind_of_class(obj, a_class):
    """
    This function returns True if the object is an instance of,
    or if the object is an instance of a class that inherited
    from, the specified class ; otherwise False.
    """

    if isinstance(obj, a_class):
        return True
    return False
