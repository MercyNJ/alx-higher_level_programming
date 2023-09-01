#!/usr/bin/python3
"""
A script that takes in a URL, sends a request to the URL
displays the body of the response,using
urllib.error.HTTPError exceptions.
"""

import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            content = response.read().decode('utf-8')
            print(content)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
