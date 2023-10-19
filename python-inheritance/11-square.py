#!/usr/bin/python3
"""Square class module"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class inheriting rectangle"""

    def __init__(self, size):
        """initialize values"""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """Area function"""
        return self.__size * self.__size

    def __str__(self):
        """__str__ module"""
        return "[Square] {}/{}".format(self.__size, self.__size)
