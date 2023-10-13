#!/usr/bin/python3
"""Class exercise concerning rectangles"""


class Rectangle:
    """This class creates rectangles"""

    def __init__(self, width=0, height=0):
        """Init function"""
        if type(width) is not int:
            raise TypeError('width must be an integer')
        elif type(height) is not int:
            raise TypeError('height must be an integer')
        elif height < 0:
            raise ValueError('height must be >= 0')
        elif width < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__height = height
            self.__width = width

    @property
    def width(self):
        """return width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """value of rectangle setter"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """return height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """value of rectangle setter"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value
