#!/usr/bin/python3
"""
   Write a recursive function that queries the Reddit API
   and returns a list containing the titles of
   all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[]):
    url = "http://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
            "User-Agent": "Reddit Hot Article Title Scraper"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return (None)

    data = response.json()

    if "data" not in data or "children" not in data["data"]:
        return (None)

    for post in data["data"]["children"]:
        hot_list.append(post["data"]["title"])

    if "after" in data:
        hot_list = recurse(subreddit, hot_list=hot_list, after=data["after"])

    return (hot_list)
