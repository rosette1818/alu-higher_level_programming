#!/bin/bash
# Send a GET request with the required header to reveal the hidden message
curl -s -H "X-HolbertonSchool-User-Id: 98" "0.0.0.0:5000/catch_me"
