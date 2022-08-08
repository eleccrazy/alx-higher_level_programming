#!/usr/bin/python3

"""
File: test_rectangle.py
Desc: This module contains all the test cases applied
      to the rectangle module in the models package.
Author: Gizachew Bayness (Elec Crazy)
Date Created: Aug 7 2022
"""

from models.rectangle import Rectangle as R
from models.base import Base as B
import unittest
import io
import sys


class TestRectangleInstanceCreation(unittest.TestCase):
    """
    This class contains all possible test cases for Rectangle
    object instantantiations.
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

    def test_y_setter(self):
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


class TestRectangleAttributeValidator(unittest.TestCase):
    """
    This class contains all possible test cases for Rectangle
    attribute validation.
    """
    def test_width_type(self):
        """ Tests the type of width attribute """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            R("hello", 2)

    def test_width_value(self):
        """ Tests the value of width attribute """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            R(0, 45)

    def test_height_type(self):
        """ Tests the type of height attribute """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            holder = R(1, [], 4, 5, 6).id

    def test_hight_value(self):
        """ Tests the value of height attribute """
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            holder = R(1, -78, 3, 4, 5).height

    def test_x_type(self):
        """ Tests the type of x attribute """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            R(1, 2, {}, 4, 5)

    def test_x_value(self):
        """ Tests the value of x attribute """
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            R(1, 2, -2)

    def test_y_type(self):
        """ Tests the type of y attribute """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            holder = R(1, 2, 3, 78.877).id

    def test_y_value(self):
        """ Tests the value of y attribute """
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            holder = R(1, 78, 3, -11, 5).height

    def test_with_proper1(self):
        """ Tests with proper values """
        r = R(1, 2, 0, 0, 3)
        self.assertEqual(0, r.x)
        self.assertEqual(3, r.id)
        self.assertEqual(r.height, 2)

    def test_with_proper2(self):
        """ Tests with proper values """
        rr = R(4, 9, 8, 77)
        self.assertEqual(77, rr.y)


class TestRectangleArea(unittest.TestCase):
    """
    This class contains all possible test cases for area
    method in the Rectangle class.
    """
    def test_area1(self):
        """ Tests area with two args """
        r = R(3, 2)
        self.assertEqual(r.area(), 6)

    def test_area2(self):
        """ Tests are with 5 args """
        r = R(8, 7, 0, 0, 12)
        self.assertEqual(r.area(), 56)

    def test_area_empty_arg(self):
        """ Tests area with no args """
        with self.assertRaises(TypeError):
            r = R()
            area = r.area()

    def test_area_one_arg(self):
        """ Tests area with one arg """
        with self.assertRaises(TypeError):
            r = R(9)
            area = r.area()

    def test_area_improper1(self):
        """ Tests area with improper value of width """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = R(0, 7)
            area = r.area()

    def test_area_improper2(self):
        """ Tests area with improper value of height """
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = R(7, -7)
            area = r.area()

    def test_area_varies(self):
        """ Tests area with updated height and width values """
        r = R(1, 2, 3, 4, 5)
        r.height = 9
        r.width = 10
        self.assertEqual(r.area(), 90)


class TestRectangleUpdators(unittest.TestCase):
    """
    This class contains all possible testcases for update method in
    the Rectangle class.
    """
    def test_update_args_zero(self):
        """ Tests no argument """
        r = R(10, 10, 10, 10, 10)
        r.update()
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r))

    def test_update_args_one(self):
        """ Tests with one argument """
        r = R(10, 10, 10, 10, 10)
        r.update(89)
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(r))

    def test_update_args_two(self):
        """ Tests with two argument """
        r = R(10, 10, 10, 10, 10)
        r.update(89, 2)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(r))

    def test_update_args_three(self):
        """ Tests with three argument """
        r = R(10, 10, 10, 10, 10)
        r.update(89, 2, 3)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r))

    def test_update_args_four(self):
        """ Tests with four arguments """
        r = R(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4)
        self.assertEqual("[Rectangle] (89) 4/10 - 2/3", str(r))

    def test_update_args_five(self):
        """ Tests with five arguments """
        r = R(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r))

    def test_update_args_six(self):
        """ Tests with 6 argument """
        r = R(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5, 6)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r))

    def test_update_args_None_id(self):
        """ Tests with id = None """
        r = R(10, 10, 10, 10, 10)
        r.update(None)
        correct = "[Rectangle] ({}) 10/10 - 10/10".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_args_None_id_and_more(self):
        """ Tests with id = None, with others """
        r = R(10, 10, 10, 10, 10)
        r.update(None, 4, 5, 2)
        correct = "[Rectangle] ({}) 2/10 - 4/5".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_args_twice(self):
        """ Tests with double update """
        r = R(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5, 6)
        r.update(6, 5, 4, 3, 2, 89)
        self.assertEqual("[Rectangle] (6) 3/2 - 5/4", str(r))

    def test_update_args_invalid_width_type(self):
        """ Tests with invalid width type """
        r = R(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid")

    def test_update_args_width_zero(self):
        """ Tests with width = 0 """
        r = R(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(89, 0)

    def test_update_args_width_negative(self):
        """ Tests with negative width """
        r = R(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(89, -5)

    def test_update_args_invalid_height_type(self):
        """ Tests with invalid height type """
        r = R(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 2, "invalid")

    def test_update_args_height_zero(self):
        """ Tests with height = 0 """
        r = R(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(89, 1, 0)

    def test_update_args_height_negative(self):
        """ Tests with negative height """
        r = R(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(89, 1, -5)

    def test_update_args_invalid_x_type(self):
        """ Tests with invalid x type """
        r = R(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(89, 2, 3, "invalid")

    def test_update_args_x_negative(self):
        """ Tests with negative x value """
        r = R(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(89, 1, 2, -6)

    def test_update_args_invalid_y(self):
        """ Tests with invalid y type """
        r = R(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(89, 2, 3, 4, "invalid")

    def test_update_args_y_negative(self):
        """ Tests with negative y value """
        r = R(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(89, 1, 2, 3, -6)

    def test_update_args_width_before_height(self):
        """ Tests with two invalid values and notice preference """
        r = R(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid", "invalid")

    def test_update_args_width_before_x(self):
        """ Tests with invalid values """
        r = R(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid", 1, "invalid")

    def test_update_args_width_before_y(self):
        """ Tests with invalid values """
        r = R(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid", 1, 2, "invalid")

    def test_update_args_height_before_x(self):
        """ Tests with invalid values """
        r = R(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 1, "invalid", "invalid")

    def test_update_args_height_before_y(self):
        """ Tests with invalid values """
        r = R(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 1, "invalid", 1, "invalid")

    def test_update_args_x_before_y(self):
        """ Tests with invalid values """
        r = R(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(89, 1, 2, "invalid", "invalid")

    def test_update_kwargs_one(self):
        """ Tests with one kwarg"""
        r = R(10, 10, 10, 10, 10)
        r.update(id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 10/10", str(r))

    def test_update_kwargs_two(self):
        """ Tests with two kwarg """
        r = R(10, 10, 10, 10, 10)
        r.update(width=2, id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 2/10", str(r))

    def test_update_kwargs_three(self):
        """ Tests with three kwarg """
        r = R(10, 10, 10, 10, 10)
        r.update(width=2, height=3, id=89)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r))

    def test_update_kwargs_four(self):
        """ Tests with four kwarg """
        r = R(10, 10, 10, 10, 10)
        r.update(id=89, x=1, height=2, y=3, width=4)
        self.assertEqual("[Rectangle] (89) 1/3 - 4/2", str(r))

    def test_update_kwargs_five(self):
        """ Tests with five kwarg """
        r = R(10, 10, 10, 10, 10)
        r.update(y=5, x=8, id=99, width=1, height=2)
        self.assertEqual("[Rectangle] (99) 8/5 - 1/2", str(r))

    def test_update_kwargs_None_id(self):
        """ Test with id = None """
        r = R(10, 10, 10, 10, 10)
        r.update(id=None)
        correct = "[Rectangle] ({}) 10/10 - 10/10".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_kwargs_None_id_and_more(self):
        """ Test with id=None and more """
        r = R(10, 10, 10, 10, 10)
        r.update(id=None, height=7, y=9)
        correct = "[Rectangle] ({}) 10/9 - 10/7".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_kwargs_twice(self):
        """ Test by double updating """
        r = R(10, 10, 10, 10, 10)
        r.update(id=89, x=1, height=2)
        r.update(y=3, height=15, width=2)
        self.assertEqual("[Rectangle] (89) 1/3 - 2/15", str(r))

    def test_update_kwargs_invalid_width_type(self):
        """ Test with invalid width type """
        r = R(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(width="invalid")

    def test_update_kwargs_width_zero(self):
        """ Test with width = 0 """
        r = R(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=0)

    def test_update_kwargs_width_negative(self):
        """ Test with negative width """
        r = R(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=-5)

    def test_update_kwargs_invalid_height_type(self):
        """ Test with invalid height type """
        r = R(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(height="invalid")

    def test_update_kwargs_height_zero(self):
        """ Test with height = 0 """
        r = R(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=0)

    def test_update_kwargs_height_negative(self):
        """ Test with negative height """
        r = R(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=-5)

    def test_update_kwargs_inavlid_x_type(self):
        """ Test with invalid x type """
        r = R(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(x="invalid")

    def test_update_kwargs_x_negative(self):
        """ Test with negative x type """
        r = R(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(x=-5)

    def test_update_kwargs_invalid_y_type(self):
        """ Test with invalid y type """
        r = R(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(y="invalid")

    def test_update_kwargs_y_negative(self):
        """ Test with negative y value """
        r = R(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(y=-5)

    def test_update_args_and_kwargs(self):
        """ Test by updating args and kwargs """
        r = R(10, 10, 10, 10, 10)
        r.update(89, 2, height=4, y=6)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(r))

    def test_update_kwargs_wrong_keys(self):
        """ Test by wrong keys of kwargs """
        r = R(10, 10, 10, 10, 10)
        r.update(a=5, b=10)
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r))

    def test_update_kwargs_some_wrong_keys(self):
        """ Test by more wrong keys of kwargs """
        r = R(10, 10, 10, 10, 10)
        r.update(height=5, id=89, a=1, b=54, x=19, y=7)
        self.assertEqual("[Rectangle] (89) 19/7 - 10/5", str(r))


class TestRectangleStdout(unittest.TestCase):
    """
    This class provides all possible test cases related with
    stdout.
    """
    @staticmethod
    def capture_stdout(rect, method):
        """
        This method captures and returns text printed to stdout.
        """
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_str_method_print_width_height(self):
        r = R(4, 6)
        capture = TestRectangleStdout.capture_stdout(r, "print")
        correct = "[Rectangle] ({}) 0/0 - 4/6\n".format(r.id)
        self.assertEqual(correct, capture.getvalue())

    def test_str_method_width_height_x(self):
        r = R(5, 5, 1)
        correct = "[Rectangle] ({}) 1/0 - 5/5".format(r.id)
        self.assertEqual(correct, r.__str__())

    def test_str_method_width_height_x_y(self):
        r = R(1, 8, 2, 4)
        correct = "[Rectangle] ({}) 2/4 - 1/8".format(r.id)
        self.assertEqual(correct, str(r))

    def test_str_method_width_height_x_y_id(self):
        r = R(13, 21, 2, 4, 7)
        self.assertEqual("[Rectangle] (7) 2/4 - 13/21", str(r))

    def test_str_method_changed_attributes(self):
        r = R(7, 7, 0, 0, [4])
        r.width = 15
        r.height = 1
        r.x = 8
        r.y = 10
        self.assertEqual("[Rectangle] ([4]) 8/10 - 15/1", str(r))

    def test_str_method_one_arg(self):
        r = R(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r.__str__(1)

    # The following test methods test the display method.
    def test_display_width_height(self):
        r = R(2, 3, 0, 0, 0)
        capture = TestRectangleStdout.capture_stdout(r, "display")
        self.assertEqual("##\n##\n##\n", capture.getvalue())

    def test_display_width_height_x(self):
        r = R(3, 2, 1, 0, 1)
        capture = TestRectangleStdout.capture_stdout(r, "display")
        self.assertEqual(" ###\n ###\n", capture.getvalue())

    def test_display_width_height_y(self):
        r = R(4, 5, 0, 1, 0)
        capture = TestRectangleStdout.capture_stdout(r, "display")
        display = "\n####\n####\n####\n####\n####\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_width_height_x_y(self):
        r = R(2, 4, 3, 2, 0)
        capture = TestRectangleStdout.capture_stdout(r, "display")
        display = "\n\n   ##\n   ##\n   ##\n   ##\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_one_arg(self):
        r = R(5, 1, 2, 4, 7)
        with self.assertRaises(TypeError):
            r.display(1)


class TestRectangleDictRepresentation(unittest.TestCase):
    """
    This class contains all possible test case for to dictinary
    method in the Rectangle class.
    """
    def test_dictionary(self):
        """ Tests for correct result of correct args """
        r = R(10, 2, 1, 9, 5)
        correct = {'x': 1, 'y': 9, 'id': 5, 'height': 2, 'width': 10}
        self.assertDictEqual(correct, r.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        """ Tests for no instance changes """
        r1 = R(10, 2, 1, 9, 5)
        r2 = R(5, 9, 1, 2, 10)
        r2.update(**r1.to_dictionary())
        self.assertNotEqual(r1, r2)

    def test_to_dictionary_arg(self):
        """ Tests for some argument to the method """
        r = R(10, 2, 4, 1, 2)
        with self.assertRaises(TypeError):
            r.to_dictionary(1)


if __name__ == "__main___":
    unittest.main()
