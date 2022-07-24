#!/usr/bin/python3

"""
File: 6-max_integer_test.py
Desc: This module provides Unittest for max_integer([..])
Author: Gizachew Bayness (Elec Crazy)
Date Created: Jul 23 2022
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    This class provides multiple functions for genrating different
    test cases based on the unittest module for the function max_integer.
    """

    def test_int_list(self):
        """
        This test function tests both positive and negative
        integer elements of the list.
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([-4, 78, 8]), 78)
        self.assertEqual(max_integer([-1, -7, -2, 0]), 0)

    def test_float_list(self):
        """
        This test function tests both positive and negative
        flaoting point elements of the list.
        """
        self.assertEqual(max_integer([1.7, 0.8, 1.8, 7.0]), 7.0)
        self.assertEqual(max_integer([-2.2, 3.7, -17.8, 7.8]), 7.8)
        self.assertEqual(max_integer([-0.3, -0.4, -7.7, -17678.9]), -0.3)

    def test_float_int(self):
        """
        This test function tests both positive and negative flating point
        and integer elements of the list.
        """
        self.assertEqual(max_integer([1, 1.1, -3, 0]), 1.1)
        self.assertEqual(max_integer([-54, 11.78]), 11.78)
        self.assertEqual(max_integer([0, -11.9, -0.8, -88898]), 0)

    def test_empty_list(self):
        """
        This test function tests an empty list.
        """
        self.assertEqual(max_integer([]), None)

    def test_with_one_element(self):
        """
        This test function tests a list with only one element.
        """
        self.assertEqual(max_integer([33]), 33)
        self.assertEqual(max_integer([-5]), -5)
        self.assertEqual(max_integer([-0.87]), -0.87)
        self.assertEqual(max_integer([87.889]), 87.889)

    def test_strings(self):
        """
        This test function tests a list of characters or string based on their
        ascii values.
        """
        self.assertEqual(max_integer("python"), 'y')
        self.assertEqual(max_integer("Hello World"), 'r')

    def test_empty(self):
        """
        This test function tests an empty string.
        """
        self.assertEqual(max_integer(""), None)

    def test_list_of_strings(self):
        """
        This test function tests a list of strings
        """
        self.assertEqual(max_integer(["He", "how", "lovely", "you"]), "you")


if __name__ == '__main__':
    unittest.main()
