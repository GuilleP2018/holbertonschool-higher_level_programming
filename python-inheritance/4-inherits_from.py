#!/usr/bin/python3
"""Module checks if Obj is from a subclass"""


def inherits_from(obj, a_class):
    """checks if obj is a from a subclass of a_class"""
    if issubclass(obj, a_class):
        return True
    else:
        return False
