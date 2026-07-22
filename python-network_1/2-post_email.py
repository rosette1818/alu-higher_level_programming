#!/usr/bin/python3
"""Send a POST request to a URL with an email parameter using urllib.

This module takes a URL and an email address as command line
arguments, sends a POST request to the URL with the email as a
parameter, and displays the utf-8 decoded body of the response.
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({"email": email}).encode("utf-8")
    req = urllib.request.Request(url, data=data)
    with urllib.request.urlopen(req) as response:
        body = response.read()
        print(body.decode("utf-8"))
