#!/usr/bin/python3
"""Function that return an object"""


import json


def from_json_string(my_str):
    """Funtion that return an object"""

    return json.loads(my_str)
