#!/usr/bin/python3
"""
This Python script takes in a URL and an email address,
sends a POST request to the passed URL with the email
as a parameter, and finally displays the body of the response.
"""

if __name__ == "__main__":
    from requests import post as p
    from sys import argv

    req = p(argv[1], data={'email': argv[2]})
    print(req.text)
