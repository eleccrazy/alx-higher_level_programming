#!/usr/bin/python3

"""
File: test_rectangle.py
Desc: This module contains all the test cases applied
      to the rectnagle module in the models package.
Author: Gizachew Bayness (Elec Crazy)
Date Created: Aug 7 2022
"""

from models.rectangle import Rectangle as R
from models.base import Base as B
import unittest


class TestRectangle(unittest.TestCase):
    """
    This class contains all possible test cases.
    """

    def test_two_objects(self):
        """ Tests two objects """
        r1 = R(2, 3)
        r2 = R(4, 5)
        self.assertEqual(r1.id, r2.id - 1)

    def test_three_objects(self):
        """ Tests three objects """
        r1 = R(1, 1)
        r2 = R(2, 3)
        r3 = R(4, 2)
        self.assertEqual(r3.id, r1.id + 2)

    def test_four_objects(self):
        """ Tests four objects """
        r1 = R(1, 1)
        r2 = R(2, 3)
        r3 = R(4, 2)
        r4 = R(8, 9)
        self.assertEqual(r1.id, r4.id - 3)
        self.assertEqual(r2.id, r3.id - 1)

    def test_width_getter(self):
        """ tests width getter """
        r = R(1, 2, 3, 4, 5)
        self.assertEqual(r.width, 1)

    def test_width_setter(self):
        """ Tests width setter """
        r = R(1, 8)
        r.width = 80
        self.assertEqual(80, r.width)

    def test_height_getter(self):
        """ Tests height getter """
        r = R(1, 8)
        self.assertEqual(8, r.height)

    def test_height_setter(self):
        """ Tests height setter """
        r = R(77, 88)
        r.height = 3
        self.assertEqual(3, r.height)

    def test_x_getter(self):
        """ Tests x getter """
        r = R(1, 9, 7, 8)
        self.assertEqual(r.x, 7)

    def test_x_setter(self):
        """ Tests x setter """
        r = R(1, 98)
        r.x = 789
        self.assertEqual(r.x, 789)

    def test_y_getter(self):
        """ Tests x getter """
        r = R(1, 9, 7, 8)
        self.assertEqual(r.y, 8)

    def test_x_setter(self):
        """ Tests x setter """
        r = R(1, 98)
        r.y = 789
        self.assertEqual(r.y, 789)

    def test_with_id1(self):
        """ Tests with Id """
        r = R(1, 2, 3, 4)
        r1 = R(3, 8, 7, 1, 9)
        r2 = R(3, 4)
        self.assertEqual(r1.id, 9)
        self.assertEqual(r2.id, r.id + 1)

    def test_with_id2(self):
        """ Tests with Id 2"""
        self.assertEqual(R(1, 2, 3, 4, 1045).id, 1045)

    def test_one_arg(self):
        """ Tests with one arg """
        with self.assertRaises(TypeError):
            R(1)

    def test_no_arg(self):
        """ Tests with no args """
        with self.assertRaises(TypeError):
            R()

    def test_6_arg(self):
        """ Tests with 6 args """
        with self.assertRaises(TypeError):
            R(1, 2, 3, 4, 5, 6)

    def test_private_height(self):
        """ Tests accessing private height """
        with self.assertRaises(AttributeError):
            R(1, 2, 3, 4, 5).__height

    def test_private_width(self):
        """ Tests accessing private width """
        with self.assertRaises(AttributeError):
            R(1, 2, 3, 4, 5).__width

    def test_private_x(self):
        """ Tests accessing private x """
        with self.assertRaises(AttributeError):
            R(1, 2, 3, 4, 5).__x

    def test_private_y(self):
        """ Tests accessing private y """
        with self.assertRaises(AttributeError):
            R(1, 2, 3, 4, 5).__y

    def test_private_nb(self):
        """ Tests accessign private id """
        with self.assertRaises(AttributeError):
            nb_objects = B(3).__nb_objects

    def test_isinstance_rectangle(self):
        """ Tests the type of the Rectangle class """
        self.assertIsInstance(R(1, 2, 3, 4, 5), B)


if __name__ == "__main___":
    unittest.main()
