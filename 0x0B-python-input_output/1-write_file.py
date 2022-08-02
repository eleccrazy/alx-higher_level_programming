#!/usr/bin/python3

"""
File: 1-write_file.py
Desc: This module deals with writing to files.
Author: Gizachew Bayness (Elec Crazy)
Date Created: Aug 2 2022
"""


def write_file(filename="", text=""):
    """
    This function writes a string to a text file (UTF8) and
    returns the number of characters written
    """

    with open(filename, "w", encoding="utf8") as my_file:
        return (my_file.write(text))
