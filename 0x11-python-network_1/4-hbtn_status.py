#!/usr/bin/python3
"""This python module contains a script  that fetches
https://alx-intranet.hbtn.io/status"""
from requests import get


if __name__ == "__main__":
    result = get("https://alx-intranet.hbtn.io/status").text
    print("Body response:")
    print("\t- type: {}".format(type(result)))
    print("\t- content: {}".format(result))
