#!/usr/bin/python3
"""Module for append_write method."""


def append_write(filename="", text=""):
    """Method for append_write.

    Args:
        filename name of file. Defaults to "".
        text text to write in file. Defaults to "".
    """
    with open(filename, "a", encoding='utf-8') as f:
        return f.write(text)
