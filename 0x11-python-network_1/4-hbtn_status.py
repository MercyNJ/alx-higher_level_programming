#!/usr/bin/python3
"""
A script that fetches https://alx-intranet.
hbtn.io/status using requests package.
"""

import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    try:
        response = requests.get(url)
        response.raise_for_status()

        print("Body response:")
        print("\t- type: {}".format(type(response.text)))
        print("\t- content: {}".format(response.text))
    except requests.exceptions.RequestException as e:
        print("Error:", e)
