#!/usr/bin/python3

"""
File: base.py
Desc: This module contains a single class calld Base.
Author: Gizachew Bayness (Elec Crazy)
Date Created: Aug 6 2022
"""


class Base:
    """
    The base for all other classes in this project.
    """
    __nb_objects = 0

    def __init__(self, id=0):
        """
        This function instantantiates all the attributes.
        """
        if id == 0 or id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
