#!/usr/bin/python3
"""
This Python script fetches https://alx-intranet.hbtn.io/status
"""

if __name__ == "__main__":
    from urllib import request as r

    url = "https://alx-intranet.hbtn.io/status"
    with r.urlopen(url) as response:
        html = response.read()

    print("Body response:")
    print("\t- type:", type(html))
    print("\t- content:", html)
    print("\t- utf8 content:", (html.decode("utf-8")))
