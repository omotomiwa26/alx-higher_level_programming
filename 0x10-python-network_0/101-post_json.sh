#!/bin/bash
# This Bash script sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
curl -sL -X POST -H 'Content-Type: application/json' -d "$([ -f "$2" ] && cat "$2")" "$1"
