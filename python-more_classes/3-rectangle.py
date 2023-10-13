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

    def area(self):
        """return are of rectangle"""
        area_rec = self.__height * self.__width
        return area_rec

    def perimeter(self):
        """retrieve perimeter of rec"""
        if self.__width == 0 or self.__height == 0:
            perimeter_rec = 0
            return perimeter_rec
        else:
            perimeter_rec = (self.__width * 2) + (self.__height * 2)
            return perimeter_rec

    def __str__(self):
        """return string of rec"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rec = ""
        for i in range(self.__height):
            rec += "#" * self.__width
            if i < self.__height - 1:
                rec += "\n"
        return rec
