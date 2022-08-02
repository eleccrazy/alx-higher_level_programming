#!/usr/bin/python3

"""
File: 5-save_to_json_file.py
Desc: This module deals with both json and writing files.
Author: Gizachew Bayness (Elec Crazy)
Date Created: Aug 2 2022
"""
from json import dumps as d


def save_to_json_file(my_obj, filename):
    """
    This function writes an Object to a text file,
    using a JSON representation
    """

    with open(filename, "w", encoding="utf8") as my_file:
        my_file.write(d(my_obj))
