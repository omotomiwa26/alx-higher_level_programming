#!/usr/bin/python3
"""
This Python script 2 arguments(repository name & owner name)
then list 10 commits (from the most recent to oldest)
of the repository
"""

if __name__ == "__main__":
    from requests import get
    from sys import argv

    url = F'https://api.github.com/repos/{argv[2]}/{argv[1]}/commits'
    req = get(url)
    if req.status_code >= 400:
        print('None')
    else:
        for cmt in req.json()[:10]:
            print(F"{cmt.get('sha')}: {cmt.get('commit')['author']['name']}")
