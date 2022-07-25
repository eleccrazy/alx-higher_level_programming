#!/usr/bin/python3

"""
File: 9-rectangle.py
Desc: This file contains a single class defination called Rectangle
Author: Gizachew Bayness (Elec Crazy)
Date Created: Jul 25, 2022
"""


class Rectangle():
    """
    This is a class defination called Rectangle.
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        This method retrives the value of attribute width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        This method sets the value of the attribute height.
        """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """
        This method retrives the value of attribute height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        This method sets the value of the attribute height.
        """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
        else:
            raise TypeError("height must be an integer")

    def area(self):
        """
        This method computes the area of rectangle based on the
        height and width value.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        This method computes the permeter of rectangle based on
        the height and width value.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Nicely printable string representation of an object of class
        rectangle.
        """
        ret_val = ""
        if (self.__height == 0 or self.__width == 0):
            return ret_val
        for i in range(self.__height):
            [print('#', end="") for ch in range(self.__width)]
            if i < self.__height - 1:
                print("")
        return ret_val

    def __repr__(self):
        """
        An instance method that returns an official string representation
        of an instance.
        """
        ret_val = f'Rectangle({self.__width}, {self.__height})'
        return ret_val

    def __del__(self):
        """
        An instance method that deletes an instance of the class Rectangle.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        This static method compares two rectangle instnanses based on their
        Area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area1 = rect_1.area()
        area2 = rect_2.area()

        if area1 >= area2:
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        This class method returns a new Rectangle instance with
        width == height == size
        """
        return cls(size, size)
