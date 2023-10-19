#!/usr/bin/python3
"""Checks if object is of the same class"""


def is_same_class(obj, a_class):
    """checks if obj is exactly the same and return true, otherwise false"""
    if type(obj) == a_class:
        return True
    else:
        return False
