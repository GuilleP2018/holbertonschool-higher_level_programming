#!/usr/bin/python3
"""Module for write file method."""


def write_file(filename="", text=""):
    """Method for write file.

    Args:
        filename name of file. Defaults to "".
        text text to write in file. Defaults to "".
    """
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(text)
