#!/usr/bin/python3
"""
This Python script fetches https://alx-intranet.hbtn.io/status
"""

if __name__ == "__main__":
    import requests as r

    url = "https://intranet.hbtn.io/status"
    response = r.get(url)
    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)
