#!/usr/bin/python3

"""
File: test_base.py
Desc: This module contains all possible testcases for the base.py
      modlue in the models package. It uses the standard unittest.
Author: Gizachew Bayness (Elec Crazy)
Date Created: Aug 6 2022
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseObjectCreation(unittest.TestCase):
    """
    This class provides test functions for the Base class in the
    base.py module in the models package.
    """

    def test_direct_instantation(self):
        """
        This method tests the direct creation of instances with id.
        """
        self.assertEqual(Base(6).id, 6)

    def test_float_id(self):
        """
        This method checks for float id creation.
        """
        self.assertEqual(Base(12.879).id, 12.879)

    def test_string_id(self):
        """
        This method checks for str id creation.
        """
        self.assertEqual("Elec Crazy", Base("Elec Crazy").id)

    def test_list_id(self):
        """
        This method checks for list id creation
        """
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_empty_list_id(self):
        """
        This method checks for empty list id creation
        """
        self.assertEqual([], Base([]).id)

    def test_dic_id(self):
        """
        This method checks for dictionary id creation
        """
        local = {'name': "crazy", 'interest': "hacking"}
        self.assertEqual(Base(local).id, local)

    def test_tuple_id(self):
        """
        This method checks for tuple id creation
        """
        self.assertEqual(Base((1,)).id, (1,))

    def test_object_creation(self):
        """
        This method checks for the correct creation of objects.
        """
        b = Base(9)
        self.assertEqual(b.id, 9)

    def test_two_objects(self):
        """
        This method checks two object creations without passing id
        """
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_four_objects(self):
        """
        This method checks four instantations without passing id
        """
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base()
        self.assertEqual(b4.id, b1.id + 3)
        self.assertEqual(b1.id, b3.id - 2)
        self.assertEqual(b3.id, b4.id - 1)
        self.assertEqual(b4.id, b2.id + 2)

    def test_three_objects(self):
        """
        This method checks three instantations by passing id
        """
        b1 = Base(3)
        b2 = Base(4)
        b3 = Base(100)
        self.assertEqual(b3.id, 100)
        self.assertEqual(b2.id, 4)
        self.assertEqual(b1.id, 3)

    def test_mix_objects(self):
        """
        This method checks three instantations with and without
        passing an id argument.
        """
        b1 = Base()
        b2 = Base(5)
        b3 = Base()

        self.assertEqual(b1.id, b3.id - 1)
        self.assertEqual(b2.id, 5)

    def test_None_condition(self):
        b1 = Base(None)
        b2 = Base(None)
        b3 = Base(78)
        self.assertEqual(b2.id, b1.id + 1)
        self.assertEqual(b3.id, 78)

    def test_private_one(self):
        """
        This method tests accessing of private data.
        """
        with self.assertRaises(AttributeError):
            self.assertEqual(Base.__nb_objects, 1)


class TestBaseToJsonString(unittest.TestCase):
    """
    This class provides all possible test cases for the to_json
    string method in the Base class.
    """
    def test_to_json_string_rectangle_type(self):
        """ Tests the method for correct json string """
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

    def test_to_json_string_rectangle_one_dict(self):
        """ Tests the method for the exact character length """
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([r.to_dictionary()])) == 53)

    def test_to_json_string_rectangle_two_dicts(self):
        """ Tests the method for the length double json str representation """
        r1 = Rectangle(2, 3, 5, 19, 2)
        r2 = Rectangle(4, 2, 4, 1, 12)
        list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 106)

    def test_to_json_string_square_type(self):
        """ Tests the method for the correct json string reperesentation """
        s = Square(10, 2, 3, 4)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))

    def test_to_json_string_square_one_dict(self):
        """ Tests the method with few arguments, and checks the length """
        s = Square(10, 2, 3, 4)
        self.assertTrue(len(Base.to_json_string([s.to_dictionary()])) == 39)

    def test_to_json_string_square_two_dicts(self):
        """ Tests the method with two dicts, but with four arguments """
        s1 = Square(10, 2, 3, 4)
        s2 = Square(4, 5, 21, 2)
        list_dicts = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 78)

    def test_to_json_string_empty_list(self):
        """ Tests the method with empty list """
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_none(self):
        """ Tests the method with None """
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_no_args(self):
        """ Tests the method with no argument """
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_more_than_one_arg(self):
        """ Tests the method itself with two argmetns """
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)


if __name__ == '__main__':
    unittest.main()
