#!/usr/bin/python3
"""
A script that  fetches https:
    //alx-intranet.hbtn.io/status using urllib.
"""

import urllib.request

if __name__ == "__main__":
    request = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(request) as response:
        body = response.read()
        print("Body response:")
        print("\t- type:", type(body))
        print("\t- content:", repr(body))
        print("\t- utf8 content:", body.decode("utf-8"))
