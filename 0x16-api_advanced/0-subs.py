#!/usr/bin/python3
""" function that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    If an invalid subreddit is given, the function should return 0
"""
import requests


def number_of_subscribers(subreddit):
    url = "http://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
            "User-Agent": "Reddit Subscribers Checker (by your_username)"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()

        subscribers = data["data"]["subscribers"]
        return subscribers
    else:
        return 0


if __name__ == "__main__":
    number_of_subscribers()
