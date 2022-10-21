#!/usr/bin/python3
"""This python module contains a script takes in a URL, sends
a request to the URL and displays the body of the response."""
from sys import argv
from requests import get


if __name__ == "__main__":
    result = get(argv[1])
    code = result.status_code

    if code < 400:
        print(result.text)
    else:
        print("Error code: {}".format(code))
