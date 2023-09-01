#!/usr/bin/python3
"""
A script that  takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

    url = "http://0.0.0.0:5000/search_user"
    payload = {"q": letter}

    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()

        try:
            data = response.json()
            if data:
                print("[{}] {}".format(data.get("id"), data.get("name")))
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")
    except requests.exceptions.RequestException as e:
        print("Error:", e)
