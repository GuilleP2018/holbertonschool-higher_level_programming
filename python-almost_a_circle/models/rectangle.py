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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns area calculation for rectangle instance"""
        return (self.width * self.height)

    def display(self):
        """prints in stdout the rectangle instance with '#'
        with offsets x and y taken into account"""
        for vertical in range(self.__y):
            print("")
        for row in range(self.__height):
            print(" "*self.__x, end="")
            print("#"*self.__width)

    def __str__(self):
        """override __str__ with new string in the format
        [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return (f"[Rectangle] ({self.id}) "
                f"{self.x}/{self.y} - {self.width}/{self.height}")

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute of Rectangle"""
        attr_list = ["id", "width", "height", "x", "y"]
        if args and len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.__width = args[i]
                if i == 2:
                    self.__height = args[i]
                if i == 3:
                    self.__x = args[i]
                if i == 4:
                    self.__y = args[i]
        else:
            for kw in kwargs:
                if kw == "id":
                    self.id = (kwargs[kw])
                if kw == "width":
                    self.__width = (kwargs[kw])
                if kw == "height":
                    self.__height = (kwargs[kw])
                if kw == "x":
                    self.__x = (kwargs[kw])
                if kw == "y":
                    self.__y = (kwargs[kw])

    def to_dictionary(self):
        """returns dictionary representation of a Rectangle"""
        dict_rep = {}
        dict_rep["id"] = self.id
        dict_rep["width"] = self.__width
        dict_rep["height"] = self.__height
        dict_rep["x"] = self.__x
        dict_rep["y"] = self.__y
        return dict_rep
