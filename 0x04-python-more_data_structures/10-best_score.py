#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary is None or not isinstance(a_dictionary, dict):
        return None
    keys = list(a_dictionary.keys())
    index = 0
    values = list(a_dictionary.values())
    large = values[0]
    for num in values:
        if num > large:
            large = num
    for la in values:
        if la == large:
            break
        index += 1
    return keys[index]
