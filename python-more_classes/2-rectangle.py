#!/usr/bin/python3
"""Define a class Rectangle."""


class Rectangle:
    """Class Rectangle that defines a rectangle."""

    def __init__(self, width=0, height=0):
        """Initializes the data."""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Retieves the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width to a value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retieves the heigth"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the heigth to a value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return current rectangle area"""
        return self.__height * self.__width

    def perimeter(self):
        """Return current rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2
