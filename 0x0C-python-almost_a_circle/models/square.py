#!/usr/bin/python3

"""
File: square.py
Desc: This modlue contains a class called Square that
      inherits from the Recatangle class in the rectangle
      module.
Author: Gizachew Bayness (Elec Crazy)
Date Created: Aug 7 2022
"""
from models.rectangle import Rectangle as R


class Square(R):
    """
    This square class represents a square model, and inherits
    from the Rectangle class model in the models package.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        This method instantantiates instance attributes of
        the square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Getter method for size attribute """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter method for size attribute """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Returns the string representation of a Square object.
        """
        string = "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.size)
        return string

    def update(self, *args, **kwargs):
        """
        This mehod assigns instance attributes of the square class.
        """

        if args:
            length = len(args)
            self.id = args[0]
            if length > 1:
                self.width = args[1]
                self.height = args[1]
                if length > 2:
                    self.x = args[2]
                    if length > 3:
                        self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'y':
                    self.y = value
                elif key == 'x':
                    self.x = value
                elif key == 'size':
                    self.width = value
                    self.height = value
                else:
                    pass

    def to_dictionary(self):
        """
        This method returns the dictionary representation
        of a Square.
        """
        dict_reper = {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }

        return dict_reper
