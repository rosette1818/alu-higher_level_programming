#!/usr/bin/python3
"""Fetch https://intranet.hbtn.io/status using the requests package.

This module fetches the status endpoint and displays the type and
content of the response body.
"""
import requests


if __name__ == "__main__":
    response = requests.get("https://intranet.hbtn.io/status")
    body = response.text
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
