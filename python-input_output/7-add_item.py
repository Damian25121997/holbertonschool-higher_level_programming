#!/usr/bin/python3
"""Function adds all arguments to a Python list,
and then save them to a file"""


import json
import sys
import os.path


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


file = 'add_item.json'
myList = []

if os.path.exists(file) and os.path.getsize(file) > 0:
    myList = load_from_json_file(file)

if len(sys.argv) > 1:
    for arg in sys.argv[1:]:
        myList.append(arg)

save_to_json_file(myList, file)
