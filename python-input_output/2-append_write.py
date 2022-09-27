#!/usr/bin/python3
"""Function thats appends a string to a text file."""


def append_write(filename="", text=""):
    """Function thats appends a string to a text file."""

    with open(filename, 'a+') as file:
        return file.write(text)
