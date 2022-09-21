#!/usr/bin/python3
"""Define the print the first name and last name"""


def say_my_name(first_name, last_name=""):
    """Function print the first name and last name.
    Args:
        first_name: is a name.
        last_name: is a last name.
    Return:
        Always.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
