#!/usr/bin/python3

"""
File: 3-say_my_name.py
Desc: This module supplies one function called say_my_name.
Author: Gizachew Bayness (Elec Crazy)
Date Created: Jul 22 2022
"""


def say_my_name(first_name, last_name=""):
    """
    This function that prints the name of a person.
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
