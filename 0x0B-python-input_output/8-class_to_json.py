#!/usr/bin/python3

"""
File: 8-class_to_json.py
Desc: This module deals with classes and json
Author: Gizachew Bayness (Elec Crazy)
Date Created: Aug 2 2022
"""


def class_to_json(obj):
    """
    This function returns the dictionary description with
    simple data structure (list, dictionary, string, integer
    and boolean) for JSON serialization of an object
    """
    return obj.__dict__
