#!/bin/bash
# This Bash script sends a request to a URL passed as an argument, and displays only the status code of the response.
curl -s -w "%{response_code}" -o /dev/null "$1"
