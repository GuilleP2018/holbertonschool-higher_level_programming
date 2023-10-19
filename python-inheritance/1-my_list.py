#!/usr/bin/python3
"""create a subclass that inherits from a class"""


class MyList(list):
    """class list"""

    def print_sorted(self):
        """prints a sorted self"""
        print('{}'.format(sorted(self)))
