#!/usr/bin/python3
"""Send a request to a URL and display the X-Request-Id header value.

This module takes a URL as a command line argument, sends a request
to it using requests, and prints the value of the X-Request-Id
header found in the response.
"""
import sys
import requests


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print(response.headers.get("X-Request-Id"))
