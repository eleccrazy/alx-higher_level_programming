#!/usr/bin/python3

"""
File: 100-matrix_mul.py
Desc: This file supplies one function called matrix_mul
Author: Gizachew Bayness (Elec Crazy)
Date Created: Jul 23 2022
"""


def matrix_mul(m_a, m_b):
    """
    This function multiplies two matrices.
    """
    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    if type(m_b) != list:
        raise TypeError("m_b must be a list")
    if not all(type(lists) == list for lists in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(type(lists) == list for lists in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if not (all(type(item) in [int, float] for item in [item for lists
            in m_a for item in lists])):
        raise TypeError("m_a should contain only integers or floats")
    if not (all(type(item) in [int, float] for item in [item for lists
            in m_b for item in lists])):
        raise TypeError("m_b should contain only integers or floats")
    if not all(len(lists) == len(m_a[0]) for lists in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(lists) == len(m_b[0]) for lists in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    for_calc = []
    for r in range(len(m_b[0])):
        new_row = []
        for c in range(len(m_b)):
            new_row.append(m_b[c][r])
        for_calc.append(new_row)

    new_matrix = []
    for row in m_a:
        new_row = []
        for col in for_calc:
            prod = 0
            for i in range(len(for_calc[0])):
                prod += row[i] * col[i]
            new_row.append(prod)
        new_matrix.append(new_row)

    return new_matrix
