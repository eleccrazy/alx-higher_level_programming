#!/usr/bin/python3
"""This python module contains a script  that takes your GitHub
credentials (username and password) and uses the GitHub API to
display your id"""
from sys import argv
from requests import get, auth


if __name__ == "__main__":
    auth = auth.HTTPBasicAuth(argv[1], argv[2])
    result = get("https://api.github.com/user", auth=auth)
    print(result.json().get("id"))
