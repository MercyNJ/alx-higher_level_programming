#!/bin/bash
# A script that  takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response.
# A header variable X-School-User-Id must be sent with the value 98.

url=$1
curl -s -H "X-School-User-Id: 98" "$url"
