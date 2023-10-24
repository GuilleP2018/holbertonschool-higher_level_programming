#!/usr/bin/python3
"""Rectangle Module"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class inheriting from Base"""
    __width = 0
    __height = 0
    __x = 0
    __y = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        """Init function"""
        super().__init__(id)
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x <= 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y <= 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    @property
    def width(self):
        """width property"""
        return self.__width

    @property
    def height(self):
        """height property"""
        return self.__height

    @property
    def x(self):
        """x property"""
        return self.__x

    @property
    def y(self):
        """y property"""
        return self.__y

    @width.setter
    def width(self, value):
        """Width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value <= 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value <= 0:
            raise ValueError("y must be >= 0")
        self.__y = value
