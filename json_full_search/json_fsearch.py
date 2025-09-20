"""
##############################################
File: json_fsearch.py
Project: json-full-search
Desc:
File Created: Monday, 9th December 2024 11:20:04 pm
Author: Leoncio López (leobip27@gmail.com)
-----
Last Modified: Monday, 9th December 2024 11:21:03 pm
Modified By: Leoncio López (leobip27@gmail.com>)
-----
Copyright 2024 leobip, alfa-sistemas
################################################
"""

import json


def json_full_search(obj, search_key):
    if search_key in obj:
        return obj[search_key]

    for val in obj.values():
        if isinstance(val, dict):
            item = json_full_search(val, search_key)
            if item is not None:
                return item


def read_json_file(file_path, search_key):
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            return json_full_search(data, search_key)
    except json.JSONDecodeError:
        print(f"The file at {file_path} is not a valid JSON.")
    with open(file_path, "r") as file:
        data = json.load(file)
        return json_full_search(data, search_key)


# Example usage
file_path = "test_data.json"
search_key = "name"
result = read_json_file(file_path, search_key)

if result is not None:
    print(f"The value of '{search_key}' is: {result}")