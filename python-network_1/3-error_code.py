#!/usr/bin/python3
"""Send a request to a URL and display the body or the error code.

This module takes a URL as a command line argument, sends a request
to it using urllib, and displays the utf-8 decoded body of the
response. If an HTTPError occurs, it prints the HTTP status code
instead.
"""
import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            print(body.decode("utf-8"))
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
