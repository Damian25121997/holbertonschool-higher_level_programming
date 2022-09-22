#!/usr/bin/python3
"""Define a class Rectangle."""


class Rectangle:
    """Class Rectangle that defines a rectangle."""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes the data."""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        string_a = ""
        for x in range(self.__height):
            for z in range(self.__width):
                string_a += str(self.print_symbol)
            if x < (self.height - 1):
                string_a += '\n'
        return string_a

    def __repr__(self):
        return "Rectangle(" + str(self.width) + \
            ", " + str(self.__height) + ")"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
