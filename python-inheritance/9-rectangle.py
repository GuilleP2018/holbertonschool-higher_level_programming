#!/usr/bin/python3
"""Create class that inherits from basegeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class rectangle inheriting basegeometry"""

    def __init__(self, width, height):
        """instatiation of width and height"""
        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)

    def area(self):
        """area calculator"""
        return self.__width * self.__height

    def __str__(self):
        """__str__ module"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
