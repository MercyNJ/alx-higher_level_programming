#!/usr/bin/python3
"""
A script that takes in a URL, sends a request to the URL
displays the body of the response,using
requests package.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        response = requests.get(url)

        if response.status_code >= 400:
            print("Error code:", response.status_code)
        else:
            print(response.text)
    except requests.exceptions.RequestException as e:
        print("Error:", e)
