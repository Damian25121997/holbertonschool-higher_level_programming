#!/usr/bin/python3
"""Function that reads a text file"""


def read_file(filename=""):
    """Read a text file"""

    with open(filename) as file:
        text = file.read()
        print(text, end="")
