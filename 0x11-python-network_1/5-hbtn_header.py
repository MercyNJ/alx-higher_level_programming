#!/usr/bin/python3
"""
A script that  takes in a URL, sends a request to the URL &
displays the value of the variable X-Request-Id in the
response header using requests package.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        response = requests.get(url)
        response.raise_for_status()

        x_request_id = response.headers.get("X-Request-Id")
        if x_request_id:
            print(x_request_id)
    except requests.exceptions.RequestException as e:
        print("Error:", e)
