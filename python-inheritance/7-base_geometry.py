#!/usr/bin/python3
"""Write an empty class"""


class BaseGeometry:
    """Class"""

    def area(self):
        """Raise an Exception error"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
