#!/bin/bash
# Send a GET request to the given URL with a custom header and print the body
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
