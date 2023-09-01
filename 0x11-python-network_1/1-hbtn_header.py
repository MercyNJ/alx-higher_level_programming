#!/usr/bin/python3
"""
A script that takes in a URL, sends a request to the URL
& displays the value of the X-Request-Id variablein header of response.
"""

import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            x_request_id = response.getheader("X-Request-Id")
            if x_request_id:
                print(x_request_id)
    except urllib.error.URLError as e:
        print("Error:", e)
