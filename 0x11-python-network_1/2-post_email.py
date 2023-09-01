#!/usr/bin/python3
"""
A script that takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter.
"""

import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = {"email": email}
    data = urllib.parse.urlencode(data).encode('utf-8')

    try:
        with urllib.request.urlopen(url, data=data) as response:
            content = response.read().decode('utf-8')
            print(content)
    except urllib.error.URLError as e:
        print("Error:", e)
