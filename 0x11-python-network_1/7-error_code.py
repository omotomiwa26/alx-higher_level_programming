#!/usr/bin/python3
"""
This Python script takes in a URL, sends a request to the URL
and displays the body of the response.
"""

if __name__ == "__main__":
    from requests import get as g
    from sys import argv as a

    req = g(a[1])
    if req.status_code >= 400:
        print(F"Error code: {req.status_code}")
    else:
        print(req.text)
