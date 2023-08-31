#!/bin/bash
# A script that sends a request to a URL passed as an argument, and displays only the status code of the response.
# Cant use pipe, ;, && and has to use curl.

curl -s -o /dev/null -w "%{http_code}" "$1"
