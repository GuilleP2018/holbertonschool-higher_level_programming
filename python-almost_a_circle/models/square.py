#!/usr/bin/python3
"""square module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """init function"""
        super().__init__(id, x, y, size, size)

    def __str__(self):
        """ string representation of square """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """getter"""
        return self.__width

    @size.setter
    def size(self, value):
        """setter"""
        if not isinstance(value, int):
            raise ValueError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be > 0")
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """Update func"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
                self.__height = args[1]
            if len(args) >= 3:
                self.__x = args[2]
            if len(args) >= 4:
                self.__y = args[3]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.__width = kwargs['size']
                self.__height = kwargs['size']
            if 'x' in kwargs:
                self.__x = kwargs['x']
            if 'y' in kwargs:
                self.__y = kwargs['y']

    def to_dictionary(self):
        """dictionary func"""
        return {'id': self.id, 'size': self.__width,
                'x': self.__x, 'y': self.__y}
