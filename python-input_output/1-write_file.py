#!/usr/bin/python3
"""Function thats writes a string to a text file"""


def write_file(filename="", text=""):
    """Function write a sstring to a text file"""

    with open(filename, 'w+') as file:
        return file.write(text)
