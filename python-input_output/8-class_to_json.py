#!/usr/bin/python3
"""Function return the dictionary description with simple data structure"""

def class_to_json(obj):
    """Return the dictionary description"""

    return obj.__dict__
