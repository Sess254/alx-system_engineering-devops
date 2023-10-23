#!/usr/bin/python3
""" script to export data in the CSV format
"""
import requests
import sys


def export_to_csv(uid):
    """ Gathers and prints data from a JSON PLACHOLDER API in CSV format """
    base = "https://jsonplaceholder.typicode.com/"
    user = requests.get(base + "users/" + uid).json()
    userTodos = requests.get(base + "todos", params={"userId": uid}).json()
    with open("{}.csv".format(uid), 'w', encoding="utf-8") as f:
        for _ in userTodos:
            rows = '"{}","{}","{}","{}"\n'.format(
                    uid, user.get("username"), _.get("completed"),
                    _.get("title"))
            f.write(rows)


if __name__ == "__main__":
    export_to_csv(sys.argv[1])
