import json as j
#!/usr/bin/python3
"""
This module returns the JSON 
representation of an object (string)
"""


def to_json_string(my_obj):
    """
    Define and initialise the JSON
    object
    """
    json_string = j.dumps(my_obj)
    return json_string

