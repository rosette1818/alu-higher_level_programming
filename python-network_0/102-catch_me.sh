#!/bin/bash
# Makes a request that returns "You got me!"
curl -sLX PUT 0.0.0.0:5000/catch_me -H "Origin: HolbertonSchool"
