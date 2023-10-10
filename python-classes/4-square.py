#!/usr/bin/python3
"""This module contains a square class"""


class Square:
    """This class defines a square"""

    def __init__(self, size=0):
        """initializes the data"""
        self.__size = size

    @property
    def size(self):
        """Property"""
        return self.__size

    @size.setter
    def size(self, value):
        """Size setter"""
        if not isinstance(value, int):
            raise TypeError("size must be an int")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """generates the area"""
        return self.__size ** 2
