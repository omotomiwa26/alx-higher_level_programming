#!/usr/bin/python3
"""
This Python script fetches https://alx-intranet.hbtn.io/status
"""

if __name__ == "__main__":
    import requests as r

    url = "https://intranet.hbtn.io/status"
    req = r.get(url)

    print("Body response:")
    print("\t- type:", (type(req.text)))
    print("\t- content:", (req.text))
