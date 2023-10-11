#!/usr/bin/python3
"""
This module adds all arguments to a Python list,
and then save them to a file
"""


import json as j
from sys import argv
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

try:
    existing_list = load_from_json_file('add_item.json')
except (FileNotFoundError, j.JSONDecodeError):
    existing_list = []

new_items = argv[1:]
existing_list.extend(new_items)

save_to_json_file(existing_list, 'add_item.json')
