#!/usr/bin/python3
"""Send a POST request to the search_user endpoint with a letter.

This module takes an optional letter as a command line argument,
sends a POST request to http://0.0.0.0:5000/search_user with the
letter as the q parameter, and displays the result depending on
whether the response is valid, empty, or invalid JSON.
"""
import sys
import requests


if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    response = requests.post(
        "http://0.0.0.0:5000/search_user", data={"q": letter})
    try:
        result = response.json()
    except ValueError:
        print("Not a valid JSON")
    else:
        if not result:
            print("No result")
        else:
            print("[{}] {}".format(result.get("id"), result.get("name")))
