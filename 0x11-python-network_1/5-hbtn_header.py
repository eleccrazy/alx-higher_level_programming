#!/usr/bin/python3
"""This python module contains a script takes in a URL, sends a
request to the URL and displays the value of the variable
X-Request-Id in the response header"""
from requests import get
from sys import argv


if __name__ == "__main__":
    print(get(argv[1]).headers.get('X-Request-Id'))
