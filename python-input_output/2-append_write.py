#!/usr/bin/python3
"""Function thats appends a string to a text file"""


def write_file(filename="", text=""):
    """Function appends a sstring to a text file"""

    with open(filename, 'a+') as file:
        return file.write(text)
