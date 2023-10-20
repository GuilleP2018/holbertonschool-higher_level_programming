#!/usr/bin/python3
"""Module for load_from_json_file method."""

import json


def from_json_file(my_str):
    """returns object represented by JSON string."""
    return json.load(my_str)
