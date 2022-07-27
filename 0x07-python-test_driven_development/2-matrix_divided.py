#!/usr/bin/python3

"""
File: 2-matrix_divided.py
Desc: This module supplies one function called matrix_divided.
Author: Gizachew Bayness (Elec Crazy)
Date Created: Jul 21 2022
"""


def matrix_divided(matrix, div):
    """
    This function divides all elements of a matrix.
    """
    exc_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not(type(matrix) == list and matrix != [] and
            all(type(lists) == list for lists in matrix) and
            all(type(item) in [float, int] for item in [item
                for lists in matrix for item in lists])):
        raise TypeError(exc_msg)

    if not all(len(lists) == len(matrix[0]) for lists in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new = [list(map(lambda i: round(i / div, 2), ls)) for ls in matrix]
    return new
