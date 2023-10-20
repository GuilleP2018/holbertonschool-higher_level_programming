#!/usr/bin/python3
"""Module for from_json_string method."""

import json


def from_json_string(my_str):
    """Method for from_json_string.

    Args:
        my_str string to convert.

    Returns:
        json object.
    """
    return json.loads(my_str)
