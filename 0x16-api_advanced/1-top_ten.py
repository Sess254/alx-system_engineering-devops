#!/usr/bin/python3
"""  function that queries the Reddit API and prints the titles
     of the first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    url = "http://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
            "User-Agent": "Reddit Top Ten Posts Printer"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()

        if "data" in data and "children" in data["data"]:
            posts = data["data"]["children"][:10]
            for post in posts:
                title = post["data"]["title"]
                print(title)
    else:
        print(None)
