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
