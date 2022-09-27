#!/usr/bin/python3
"""Function that creates an object"""


import json


def load_from_json_file(filename):
    """Function that creates an object"""

    with open(filename, 'r') as file:
        return json.load(file)
