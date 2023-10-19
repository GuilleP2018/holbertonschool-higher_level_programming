#!/usr/bin/python3
"""module that checks if its from the same class or inherits from it"""


def is_kind_of_class(obj, a_class):
    """true if same class or inherits, false otherwise"""
    if type(obj) is a_class or isinstance(obj, a_class):
        return True
    else:
        return False
