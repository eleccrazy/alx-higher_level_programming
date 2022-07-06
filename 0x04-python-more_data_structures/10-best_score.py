#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    large = a_dictionary[list(a_dictionary.keys())[0]]
    big_key = list(a_dictionary.keys())[0]
    for key, value in a_dictionary.items():
        if value > large:
            large = value
            big_key = key
    return big_key
