#!/usr/bin/python3

"""
File: test_square.py
Desc: This module contains all the test cases applied
      to the square module in the models package.
Author: Gizachew Bayness (Elec Crazy)
Date Created: Aug 7 2022
"""

from models.square import Square as S
from models.base import Base as B
import unittest
import sys
import io


class TestSquareInstanceCreation(unittest.TestCase):
    """
    This class contains all possible test cases for Square
    object instantantiations.
    """

    def test_two_objects(self):
        """ Tests two objects """
        s1 = S(2)
        s2 = S(4)
        self.assertEqual(s1.id, s2.id - 1)

    def test_three_objects(self):
        """ Tests three objects """
        s1 = S(1)
        s2 = S(2)
        s3 = S(4)
        self.assertEqual(s3.id, s1.id + 2)

    def test_four_objects(self):
        """ Tests four objects """
        s1 = S(1)
        s2 = S(2)
        s3 = S(4)
        s4 = S(8)
        self.assertEqual(s1.id, s4.id - 3)
        self.assertEqual(s2.id, s3.id - 1)

    def test_size_getter(self):
        """ tests width getter """
        s = S(1, 3, 4, 5)
        self.assertEqual(s.size, 1)

    def test_size_setter(self):
        """ Tests width setter """
        s = S(8)
        s.size = 80
        self.assertEqual(80, s.size)

    def test_x_getter(self):
        """ Tests x getter """
        s = S(1, 9, 7, 8)
        self.assertEqual(s.x, 9)

    def test_x_setter(self):
        """ Tests x setter """
        s = S(1, 9, 8, 10)
        s.x = 70
        self.assertEqual(70, s.x)

    def test_y_getter(self):
        """ Tests x getter """
        s = S(1, 9, 7, 8)
        self.assertEqual(s.y, 7)

    def test_y_setter(self):
        """ Tests x setter """
        s = S(1, 98)
        s.y = 789
        self.assertEqual(s.y, 789)

    def test_with_id1(self):
        """ Tests with Id """
        s = S(1, 2, 4)
        s1 = S(3, 8, 7, 9)
        s2 = S(3, 4)
        self.assertEqual(s1.id, 9)
        self.assertEqual(s2.id, s.id + 1)

    def test_with_id2(self):
        """ Tests with Id 2"""
        self.assertEqual(S(1, 2, 3, 1045).id, 1045)

    def test_no_arg(self):
        """ Tests with no args """
        with self.assertRaises(TypeError):
            S()

    def test_6_arg(self):
        """ Tests with 6 args """
        with self.assertRaises(TypeError):
            S(1, 2, 3, 4, 5, 6)

    def test_private_height(self):
        """ Tests accessing private height """
        with self.assertRaises(AttributeError):
            S(1, 2, 4, 5).__height

    def test_private_width(self):
        """ Tests accessing private width """
        with self.assertRaises(AttributeError):
            S(1, 2, 4, 5).__width

    def test_private_x(self):
        """ Tests accessing private x """
        with self.assertRaises(AttributeError):
            S(1, 2, 4, 5).__x

    def test_private_y(self):
        """ Tests accessing private y """
        with self.assertRaises(AttributeError):
            S(1, 2, 3, 4).__y

    def test_private_nb(self):
        """ Tests accessign private id """
        with self.assertRaises(AttributeError):
            nb_objects = B(3).__nb_objects

    def test_isinstance_rectangle(self):
        """ Tests the type of the Rectangle class """
        self.assertIsInstance(S(1, 2, 3, 4), B)


class TestSquareAttributeValidator(unittest.TestCase):
    """
    This class contains all possible test cases for Square
    attribute validation.
    """
    def test_width_type(self):
        """ Tests the type of width attribute """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            S("hello", 2)

    def test_width_value(self):
        """ Tests the value of width attribute """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            S(0, 45)

    def test_height_type(self):
        """ Tests the type of height attribute """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            holder = S([], 4, 5, 6).id

    def test_hight_value(self):
        """ Tests the value of height attribute """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            holder = S(-78, 3, 4, 5).height

    def test_x_type(self):
        """ Tests the type of x attribute """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            S(1, {}, 4, 5)

    def test_x_value(self):
        """ Tests the value of x attribute """
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            S(1, -2)

    def test_y_type(self):
        """ Tests the type of y attribute """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            holder = S(1, 2, 78.877).id

    def test_y_value(self):
        """ Tests the value of y attribute """
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            holder = S(1, 78, -11, 5).height

    def test_with_proper1(self):
        """ Tests with proper values """
        s = S(1, 2, 0, 3)
        self.assertEqual(2, s.x)
        self.assertEqual(3, s.id)
        self.assertEqual(s.size, 1)

    def test_with_proper2(self):
        """ Tests with proper values """
        ss = S(4, 9, 8, 77)
        self.assertEqual(8, ss.y)


class TestSquareArea(unittest.TestCase):
    """
    This class contains all possible test cases for area
    method in the Rectangle class inherited by Square.
    """
    def test_area1(self):
        """ Tests area with two args """
        s = S(3)
        self.assertEqual(s.area(), 9)

    def test_area2(self):
        """ Tests are with 5 args """
        s = S(8, 7, 0, 12)
        self.assertEqual(s.area(), 64)

    def test_area_empty_arg(self):
        """ Tests area with no args """
        with self.assertRaises(TypeError):
            s = S()
            area = s.area()

    def test_area_one_arg(self):
        """ Tests area with one arg """
        s = S(9)
        self.assertEqual(81, s.area())

    def test_area_improper1(self):
        """ Tests area with improper value of width """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s = S(0, 7)
            area = s.area()

    def test_area_varies(self):
        """ Tests area with updated height and width values """
        s = S(8, 2, 3, 5)
        s.size = 5
        self.assertEqual(s.area(), 25)


class TestSquareUpdators(unittest.TestCase):
    """
    This class contains all possible testcases for update method in
    the Rectangle class.
    """
    def test_update_args_zero(self):
        """ Tests no argument """
        s = S(10, 10, 10, 10)
        s.update()
        self.assertEqual("[Square] (10) 10/10 - 10", str(s))

    def test_update_args_one(self):
        """ Tests with one argument """
        s = S(10, 10, 10, 10)
        s.update(89)
        self.assertEqual("[Square] (89) 10/10 - 10", str(s))

    def test_update_args_two(self):
        """ Tests with two argument """
        s = S(10, 10, 10, 10)
        s.update(89, 2)
        self.assertEqual("[Square] (89) 10/10 - 2", str(s))

    def test_update_args_three(self):
        """ Tests with three argument """
        s = S(10, 10, 10, 10)
        s.update(89, 2, 3)
        self.assertEqual("[Square] (89) 3/10 - 2", str(s))

    def test_update_args_four(self):
        """ Tests with four arguments """
        s = S(10, 10, 10, 10)
        s.update(89, 2, 3, 4)
        self.assertEqual("[Square] (89) 3/4 - 2", str(s))

    def test_update_args_six(self):
        """ Tests with 6 argument """
        s = S(10, 10, 10, 10)
        s.update(89, 2, 3, 4, 5, 6)
        self.assertEqual("[Square] (89) 3/4 - 2", str(s))

    def test_update_args_None_id(self):
        """ Tests with id = None """
        s = S(10, 10, 10, 10)
        s.update(None)
        correct = "[Square] ({}) 10/10 - 10".format(s.id)
        self.assertEqual(correct, str(s))

    def test_update_args_None_id_and_more(self):
        """ Tests with id = None, with others """
        s = S(10, 10, 10, 10)
        s.update(None, 4, 5, 2)
        correct = "[Square] ({}) 5/2 - 4".format(s.id)
        self.assertEqual(correct, str(s))

    def test_update_args_twice(self):
        """ Tests with double update """
        s = S(10, 10, 10, 10)
        s.update(89, 2, 3, 4)
        s.update(6, 5, 4, 3)
        self.assertEqual("[Square] (6) 4/3 - 5", str(s))

    def test_update_args_invalid_size_type(self):
        """ Tests with invalid width type """
        s = S(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(89, "invalid")

    def test_update_args_width_zero(self):
        """ Tests with width = 0 """
        s = S(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(89, 0)

    def test_update_args_width_negative(self):
        """ Tests with negative width """
        s = S(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(89, -5)

    def test_update_args_invalid_x_type(self):
        """ Tests with invalid x type """
        s = S(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(89, 2, "invalid")

    def test_update_args_x_negative(self):
        """ Tests with negative x value """
        s = S(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(89, 1, -6)

    def test_update_args_invalid_y(self):
        """ Tests with invalid y type """
        s = S(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(89, 2, 3, "invalid")

    def test_update_args_y_negative(self):
        """ Tests with negative y value """
        s = S(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s.update(89, 1, 2, -6)

    def test_update_args_size_before_x(self):
        """ Tests with two invalid values and notice preference """
        s = S(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(89, "invalid", "invalid")

    def test_update_args_size_before_y(self):
        """ Tests with invalid values """
        s = S(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(89, "invalid", 1, "invalid")

    def test_update_args_width_before_x(self):
        """ Tests with invalid values """
        s = S(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(89, "invalid",  "invalid")

    def test_update_args_x_before_y(self):
        """ Tests with invalid values """
        s = S(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(89, 1, "invalid", "invalid")

    def test_update_kwargs_one(self):
        """ Tests with one kwarg"""
        s = S(10, 10, 10, 10)
        s.update(id=1)
        self.assertEqual("[Square] (1) 10/10 - 10", str(s))

    def test_update_kwargs_two(self):
        """ Tests with two kwarg """
        s = S(10, 10, 10, 10)
        s.update(size=2, id=1)
        self.assertEqual("[Square] (1) 10/10 - 2", str(s))

    def test_update_kwargs_three(self):
        """ Tests with four kwarg """
        s = S(10, 10, 10, 10)
        s.update(id=89, x=1, size=2, y=3)
        self.assertEqual("[Square] (89) 1/3 - 2", str(s))

    def test_update_kwargs_None_id(self):
        """ Test with id = None """
        s = S(10, 10, 10, 10)
        s.update(id=None)
        correct = "[Square] ({}) 10/10 - 10".format(s.id)
        self.assertEqual(correct, str(s))

    def test_update_kwargs_None_id_and_more(self):
        """ Test with id=None and more """
        s = S(10, 10, 10, 10)
        s.update(id=None, size=7, y=9)
        correct = "[Square] ({}) 10/9 - 7".format(s.id)
        self.assertEqual(correct, str(s))

    def test_update_kwargs_twice(self):
        """ Test by double updating """
        s = S(10, 10, 10, 10)
        s.update(id=89, x=1, size=2)
        s.update(y=3, size=15)
        self.assertEqual("[Square] (89) 1/3 - 15", str(s))

    def test_update_kwargs_invalid_size_type(self):
        """ Test with invalid width type """
        s = S(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(size="invalid")

    def test_update_kwargs_size_zero(self):
        """ Test with width = 0 """
        s = S(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(size=0)

    def test_update_kwargs_size_negative(self):
        """ Test with negative width """
        s = S(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(size=-5)

    def test_update_kwargs_inavlid_x_type(self):
        """ Test with invalid x type """
        s = S(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(x="invalid")

    def test_update_kwargs_x_negative(self):
        """ Test with negative x type """
        s = S(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(x=-5)

    def test_update_kwargs_invalid_y_type(self):
        """ Test with invalid y type """
        s = S(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(y="invalid")

    def test_update_kwargs_y_negative(self):
        """ Test with negative y value """
        s = S(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s.update(y=-5)

    def test_update_args_and_kwargs(self):
        """ Test by updating args and kwargs """
        s = S(10, 10, 10, 10)
        s.update(89, 2, size=4, y=6)
        self.assertEqual("[Square] (89) 10/10 - 2", str(s))

    def test_update_kwargs_wrong_keys(self):
        """ Test by wrong keys of kwargs """
        s = S(10, 10, 10, 10)
        s.update(a=5, b=10)
        self.assertEqual("[Square] (10) 10/10 - 10", str(s))

    def test_update_kwargs_some_wrong_keys(self):
        """ Test by more wrong keys of kwargs """
        s = S(10, 10, 10, 10)
        s.update(size=5, id=89, a=1, b=54, x=19, y=7)
        self.assertEqual("[Square] (89) 19/7 - 5", str(s))


class TestSquareStdout(unittest.TestCase):
    """
    This class contains all possible test cases for square stdout
    """
    @staticmethod
    def capture_stdout(sq, method):
        """
        Captures and returns text printed to stdout.
        """
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(sq)
        else:
            sq.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_str_method_print_size(self):
        s = S(4)
        capture = TestSquareStdout.capture_stdout(s, "print")
        correct = "[Square] ({}) 0/0 - 4\n".format(s.id)
        self.assertEqual(correct, capture.getvalue())

    def test_str_method_size_x(self):
        s = S(5, 5)
        correct = "[Square] ({}) 5/0 - 5".format(s.id)
        self.assertEqual(correct, s.__str__())

    def test_str_method_size_x_y(self):
        s = S(7, 4, 22)
        correct = "[Square] ({}) 4/22 - 7".format(s.id)
        self.assertEqual(correct, str(s))

    def test_str_method_size_x_y_id(self):
        s = S(2, 88, 4, 19)
        self.assertEqual("[Square] (19) 88/4 - 2", str(s))

    def test_str_method_changed_attributes(self):
        s = S(7, 0, 0, [4])
        s.size = 15
        s.x = 8
        s.y = 10
        self.assertEqual("[Square] ([4]) 8/10 - 15", str(s))

    def test_str_method_one_arg(self):
        s = S(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            s.__str__(1)

    # The following methods test the display method

    def test_display_size(self):
        s = S(2, 0, 0, 9)
        capture = TestSquareStdout.capture_stdout(s, "display")
        self.assertEqual("##\n##\n", capture.getvalue())

    def test_display_size_x(self):
        s = S(3, 1, 0, 18)
        capture = TestSquareStdout.capture_stdout(s, "display")
        self.assertEqual(" ###\n ###\n ###\n", capture.getvalue())

    def test_display_size_y(self):
        s = S(4, 0, 1, 9)
        capture = TestSquareStdout.capture_stdout(s, "display")
        display = "\n####\n####\n####\n####\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_size_x_y(self):
        s = S(2, 3, 2, 1)
        capture = TestSquareStdout.capture_stdout(s, "display")
        display = "\n\n   ##\n   ##\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_one_arg(self):
        s = S(3, 4, 5, 2)
        with self.assertRaises(TypeError):
            s.display(1)


class TestSquareDictRepresentation(unittest.TestCase):
    """
    This class contains all possible test cases for to dictinary
    method in the Rectangle class.
    """
    def test_to_dictionary_output(self):
        """ Tests for correct result of correct args """
        s = S(10, 2, 1, 1)
        correct = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertDictEqual(correct, s.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        """ Tests for no instance changes """
        s1 = S(10, 2, 1, 2)
        s2 = S(1, 2, 10)
        s2.update(**s1.to_dictionary())
        self.assertNotEqual(s1, s2)

    def test_to_dictionary_arg(self):
        """ Tests for some argument to the method """
        s = S(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            s.to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
