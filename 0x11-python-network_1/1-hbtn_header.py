#!/usr/bin/python3
"""
This Python  takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response.
"""

if __name__ == "__main__":
    import urllib.request as u
    import sys as s

    with u.urlopen(s.argv[1]) as response:
        head = response.headers.get('X-Request-Id')
        print(head)
