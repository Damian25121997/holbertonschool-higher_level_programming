#!/usr/bin/python3
"""Function return True if the object is an instance of a class,
otherwise False"""


def inherits_from(obj, a_class):
    """Function return True if the object is an instance of a class,
     otherwise False"""

    return isinstance(obj, a_class) and type(obj) != a_class
