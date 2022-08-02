#!/usr/bin/python3

"""
File: 2-append_write.py
Desc: This module deals with appending a file.
Author: Gizachew Bayness (Elec Crazy)
Date Created: Aug 2 2022
"""


def append_write(filename="", text=""):
    """
    This function appends a string at the end of a text file
    (UTF8) and returns the number of characters added
    """

    with open(filename, "a", encoding="utf8") as my_file:
        return my_file.write(text)
