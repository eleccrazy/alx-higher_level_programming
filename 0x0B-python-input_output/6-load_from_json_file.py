#!/usr/bin/python3

"""
File: 6-load_from_json_file.py
Desc: This modlue deals with json strings and reading files.
Author: Gizachew Bayness (Elec Crazy)
Date Created: Aug 2 2022
"""
from json import loads as ls


def load_from_json_file(filename):
    """
    This function creates an Object from a “JSON file”
    """
    with open(filename, encoding="utf8") as my_file:
        return ls(my_file.read())
