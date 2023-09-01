#!/usr/bin/python3
"""
A script that solve this challenge.
Please list 10 commits (from the most recent to oldest) of
the repository “rails” by the user “rails”
You must use the GitHub API.
Print all commits by: `<sha>: <author name>` (one by line)
"""

import sys
import requests

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = "https://api.github.com/repos/{}/commits".format(
            owner_name + "/" + repo_name
            )

    try:
        response = requests.get(url)
        response.raise_for_status()

        commits = response.json()[:10]
        for commit in commits:
            sha = commit.get("sha")
            author_name = commit.get("commit").get("author").get("name")
            print("{}: {}".format(sha, author_name))
    except requests.exceptions.RequestException as e:
        print("Error:", e)
