#!/usr/bin/python3
"""This python module contains a script that takes in a URL and an
email address, sends a POST request to the passed URL with the
email as a parameter, and finally displays the body of the
response. """
from sys import argv
from requests import post


if __name__ == "__main__":
    payload = {'email': argv[2]}
    result = post(argv[1], data=payload)
    print(result.text)
