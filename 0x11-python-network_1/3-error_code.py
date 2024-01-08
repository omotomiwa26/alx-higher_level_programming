#!/usr/bin/python3
"""
This Pyhton script takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""

if __name__ == "__main__":
    from urllib import request as r
    from urllib.error import HTTPError as h
    from sys import argv

    try:
        with r.urlopen(argv[1]) as response:
            print(response.read().decode("utf-8", "replace"))
    except h as e:
        print(F"Error code: {e.code}")
