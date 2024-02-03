#!/usr/bin/python3
"""
This Python script takes in a URL and an email,
sends a POST request to the passed URL with the email
as a parameter, and displays the body of the response
(decoded in utf-8)
"""

if __name__ == "__main__":
    from urllib import request as r, parse as p
    from sys import argv

    value = {'email': argv[2]}
    data = p.urlencode(value)
    data = data.encode('ascii')
    req = r.Request(argv[1], data)
    with r.urlopen(req) as response:
        print(response.read().decode("utf-8", "replace"))
