#!/usr/bin/python3

"""
File: 1-my_list.py
Desc: This module contains a single class defination.
Author: Gizachew Bayness (Elec Crazy)
Date Created: Aug 1 2022
"""


class MyList(list):
    """
    A class that inherits from the list builtin class.
    """
    def __init__(self):
        """
        This method initializes the object with the
        super class init method.
        """
        super().__init__()

    def print_sorted(self):
        """
        This method prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
