#!/usr/bin/python3
"""
A script that takes GitHub credentials (username and passwd)
& uses the GitHub API to display id.
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    personal_access_token = sys.argv[2]

    url = "https://api.github.com/user"

    auth = (username, personal_access_token)

    try:
        response = requests.get(url, auth=auth)
        if response.status_code == 200:
            data = response.json()
            user_id = data.get("id")
            print(user_id)
        else:
            print(None)

    except requests.exceptions.RequestException as e:
        print("Error:", e)
