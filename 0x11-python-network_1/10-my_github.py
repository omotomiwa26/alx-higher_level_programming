#!/usr/bin/python3
"""
This Python script takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""

if __name__ == "__main__":
    from requests import get as g
    from sys import argv

    url = 'https://api.github.com/user'
    req = g(url, auth=(argv[1], argv[2]))
    if req.status_code >= 400:
        print('None')
    else:
        print(req.json().g('id'))
