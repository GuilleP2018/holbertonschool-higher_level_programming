#!/usr/bin/python3
"""Create a class base geometry"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """unimplemented area"""
        if self:
            raise Exception("area() is not implemented")
