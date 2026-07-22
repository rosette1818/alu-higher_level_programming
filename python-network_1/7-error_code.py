#!/usr/bin/python3
"""Send a request to a URL and display the body or the error code.

This module takes a URL as a command line argument, sends a request
to it using requests, and displays the body of the response. If the
status code is 400 or higher, it prints the HTTP status code instead.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
