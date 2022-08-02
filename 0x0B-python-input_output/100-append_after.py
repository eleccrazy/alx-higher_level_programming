#!/usr/bin/python3

"""
File: 100-append_after.py
Desc: This module deals with automating files.
Author: Gizachew Bayness (Elec Crazy)
Date Created: Aug 2 2022
"""


def append_after(filename="", search_string="", new_string=""):
    """
    This function inserts a line of text to a file, after each
    line containing a specific string
    """
    with open(filename, "r", encoding="utf8") as my_file:
        line_list = my_file.readlines()
        new_content = ""
        for l in line_list:
            new_content += l
            if search_string in l:
                new_content += new_string
    with open(filename, "w", encoding="utf8") as my_file:
        my_file.write(new_content)
