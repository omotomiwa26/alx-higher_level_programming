#!/bin/bash
# This Bash script takes in a URL, sends a request to that URL, and displays the size of the body of the response
<<<<<<< HEAD

curl -sI "$s1" | grep -oiE 'Content-Length: [0-9]+' | cut -d ' ' -f2
=======
curl -sI "$1" | grep -oiE 'Content-Length: [0-9]+' | cut -d ' ' -f2
>>>>>>> ec896a394220ec53bb2f18db996282a3567704a9
