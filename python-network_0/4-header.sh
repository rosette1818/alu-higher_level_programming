#!/bin/bash
# Send a GET request to the given URL with a header value (default 98)
curl -s -H "X-HolbertonSchool-User-Id: ${2:-98}" "$1"
