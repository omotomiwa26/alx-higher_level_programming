#!/usr/bin/env bash
# This Bash script takes in a URL, sends a request to that URL, and displays the size of the body of the response

url=$1

curl -sI "$url" | grep -oiE 'Content-Length: [0-9]+' | cut -d ' ' -f2
