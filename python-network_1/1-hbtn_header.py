#!/usr/bin/python3
"""Send a request to a URL and display the X-Request-Id header value.

This module takes a URL as a command line argument, sends a request
to it using urllib, and prints the value of the X-Request-Id header
found in the response.
"""
import sys
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.getheader("X-Request-Id"))
