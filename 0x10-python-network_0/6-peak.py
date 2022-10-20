#!/usr/bin/python3

"""This module contains a function that finds a peak in a list
of unsorted integers."""


def find_peak(list_of_integers):
    """This function finds a peak number in a list"""

    if list_of_integers == []:
        return None

    if len(list_of_integers) < 3:
        return max(list_of_integers)

    max_index = int(len(list_of_integers) / 2)
    peack_number = list_of_integers[max_index]

    if (peack_number > list_of_integers[max_index - 1] and
            peack_number > list_of_integers[max_index + 1]):
        return peack_number

    elif peack_number <= list_of_integers[max_index + 1]:
        return find_peak(list_of_integers[max_index + 1:])

    else:
        return find_peak(list_of_integers[:max_index])
