#!/usr/bin/python3
"""
This Python script fetches https://alx-intranet.hbtn.io/status
"""

if __name__ == "__main__":
    import urllib.request

    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        content = response.read().decode('utf-8')

    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)
