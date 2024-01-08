#!/usr/bin/python3
"""
This Python script takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""


if __name__ == "__main__":
    from requests import post as p
    from sys import argv

    q = argv[1] if len(argv) > 1 else ""
    r = p('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        dic = r.json()
        if dic == {}:
            print('No result')
        else:
            print(F"[{dic.get('id')}] {dic.get('name')}")
    except ValueError:
        print('Not a valid JSON')
