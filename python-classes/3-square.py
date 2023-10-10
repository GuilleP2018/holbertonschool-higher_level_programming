#!/usr/bin/python3
"""This module contains a square class"""


class Square:
    """This class defines a square"""

    def __init__(self, size=0):
        """initializes the data"""
        if type(size) is not int:
            raise TypeError("size must be an int")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__Square__size = size

    def area(self):
        """generates the area"""
        return self.__Square__size ** 2