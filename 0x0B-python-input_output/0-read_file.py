#!/usr/bin/python3

"""
File: 0-read_file.py
Desc: This module deals with reading files.
Author: Gizachew Bayness (Elec Crazy)
Date Created: Aug 2 2022
"""


def read_file(filename=""):
    """
    This function reads a text file (UTF8) and prints it to stdout.
    """

    with open(filename, encoding="utf8") as my_file:
        for text in my_file:
            print(text, end="")
