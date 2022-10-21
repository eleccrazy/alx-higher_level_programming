#!/usr/bin/python3
"""This python module takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter, and
displays the body of the response (decoded in utf-8)"""
from sys import argv
from urllib.request import urlopen
from urllib.parse import urlencode


if __name__ == "__main__":
    params = {'email': argv[2]}
    post_data = urlencode(params).encode('ascii')

    with urlopen(argv[1], post_data) as response:
        print(response.read().decode('utf8'))
