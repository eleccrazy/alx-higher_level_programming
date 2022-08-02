#!/usr/bin/python3

"""
File: 4-from_json_string.py
Desc: This module deals with the json object.
Author: Gizachew Bayness (Elec crazy)
Date Created: Aug 2 2022
"""
from json import loads as l


def from_json_string(my_str):
    """
    This function returns an object (Python data structure)
    represented by a JSON string
    """
    
    return l(my_str)
