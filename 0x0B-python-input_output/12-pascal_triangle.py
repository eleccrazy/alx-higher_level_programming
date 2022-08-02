#!/usr/bin/python3

"""
File: 12-pascal_triangle.py
Desc: This module shows the implementation of pascal's triangle.
Author: Gizachew Bayness (Elec Crazy)
Date Created: Aug 2 2022
"""


def pascal_triangle(n):
    """
    This function returns a list of lists of integers representing
    the Pascal’s triangle of n
    """
    if (n <= 0):
        return []
    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
