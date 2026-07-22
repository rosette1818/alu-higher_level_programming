#!/usr/bin/python3
"""Display the id of a GitHub user using Basic Authentication.

This module takes a GitHub username and a personal access token as
command line arguments, uses them to authenticate against the GitHub
API, and prints the id of the authenticated user.
"""
import sys
import requests


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    response = requests.get(
        "https://api.github.com/user", auth=(username, password))
    if response.status_code == 200:
        print(response.json().get("id"))
    else:
        print(None)
