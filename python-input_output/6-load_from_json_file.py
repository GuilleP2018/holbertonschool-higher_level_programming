#!/usr/bin/python3
"""Module for load_from_json_file method."""

import json


def load_from_json_file(filename):
    """Method for load_from_json_file.

    Args:
        filename name of file.

    Returns:
        json object.
    """
    with open(filename, encoding='utf-8') as f:
        return json.load(f)
