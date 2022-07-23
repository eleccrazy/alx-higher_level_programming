#!/usr/bin/python3

"""
File: 5-text_indentation.py
Desc: This module supplies one function called text_indentation
Author: Gizachew Bayness (Elec Crazy)
Date Created: Jul 22 2022
"""


def text_indentation(text):
    """
    This function  prints a text with 2 new lines after each of
    these characters: ., ? and :
    """
    if type(text) != str:
        raise TypeError("text must be a string")

    spaces_at_start = 0
    for ch in text:
        if ch != ' ':
            break
        spaces_at_start += 1

    index = spaces_at_start

    while index < len(text):
        print(text[index], end="")
        if text[index] == "\n" or text[index] in ".?:":
            if text[index] in ".?:":
                print("\n")
            index += 1
            while index < len(text) and text[index] == ' ':
                index += 1
            continue
        index += 1
