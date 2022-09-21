#!/usr/bin/python3
"""Define the print a square with the character #"""


def print_square(size):
    """Function print a square with the character #.
    Args:
        size: is a size lenght of the square.
    Return:
        Always.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    for x in range(size):
        for z in range(size):
            print("#", end="")
        print()
