#!/usr/bin/python3

"""
File: 100-my_int.py
Desc: This modlue contains a single class defination.
Author: Gizachew Bayness (Elec Crazy)
Date Created: Aug 1 2022
"""


class MyInt(int):
    """
    This class inherets from builtin class int.
    """

    def __ne__(self, value):
        """
        The not equal to representation of class MyInt.
        """
        return self.real == value

    def __eq__(self, value):
        """
        The equl to representation of class MyInt.
        """
        return self.real != value
