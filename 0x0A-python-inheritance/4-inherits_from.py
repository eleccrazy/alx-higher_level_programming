#!/usr/bin/python3

"""
File: 4-inherits_from.py
Desc: This file contains a single function defination.
Author: Gizachew Bayness (Elec Crazy).
Date Created: Aug 1 2022
"""


def inherits_from(obj, a_class):
    """
    This function  returns True if the object is an
    instance of a class that inherited (directly or indirectly)
    from the specified class ; otherwise False.
    """

    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    return False
