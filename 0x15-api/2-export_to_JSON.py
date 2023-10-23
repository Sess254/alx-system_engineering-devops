#!/usr/bin/python3
""" script to export data in the json format
"""
import json
import requests
import sys


def export_to_json(uid):
    """ Gathers and prints data from a JSON PLACHOLDER API in json format """
    base = "https://jsonplaceholder.typicode.com/"
    user = requests.get(base + "users/" + uid).json()
    userTodos = requests.get(base + "todos", params={"userId": uid}).json()
    with open("{}.json".format(uid), 'w', encoding="utf-8") as f:
        data = {uid: []}
        for _ in userTodos:
            rows = {"tasks": _.get("title"), "completed": _.get("completed"),
                    "username": user.get("username")}
            data[uid].append(rows)
        f.write(json.dumps(data))


if __name__ == "__main__":
    export_to_json(sys.argv[1])
