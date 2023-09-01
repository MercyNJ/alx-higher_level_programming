#!/usr/bin/python3
"""
A script that takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter.
uses requests package.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    payload = {"email": email}

    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()

        print(response.text)
    except requests.exceptions.RequestException as e:
        print("Error:", e)
