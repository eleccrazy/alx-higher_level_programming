#!/usr/bin/python3

"""
File: 101-lazy_matrix_mul.py
Desc: This module supplies one function called lazy_matrix_mul
Author: Gizachew Bayness (Elec Crazy)
Date Created: Jul 23 2022
"""
from numpy import matmul as m


def lazy_matrix_mul(m_a, m_b):
    """
    This function multiplies two matrices.
    """
    return m(m_a, m_b)
