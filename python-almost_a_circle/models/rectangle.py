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
        self.__width = width
        self.__height = height
        self.__x = x
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
        if value <= 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value <= 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns area calculation for rectangle instance"""
        return (self.width * self.height)

    def display(self):
        """prints in stdout the rectangle instance with '#'
        with offsets x and y taken into account"""
        for vertical in range(self.y):
            print("")
        for row in range(self.height):
            print(" "*self.x, end="")
            print("#"*self.width)

        def __str__(self):
            """override __str__ with new string in the format
            [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
            str_rep = "[Rectangle] ({}) {}/{} - {}/{}".format(
                str(self.id), str(self.x), str(self.y),
                str(self.width), str(self.height))
            return (str_rep)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute of Rectangle"""
        attr_list = ["id", "width", "height", "x", "y"]
        if args and len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.width = args[i]
                if i == 2:
                    self.height = args[i]
                if i == 3:
                    self.x = args[i]
                if i == 4:
                    self.y = args[i]
        else:
            for kw in kwargs:
                if kw == "id":
                    self.id = (kwargs[kw])
                if kw == "width":
                    self.width = (kwargs[kw])
                if kw == "height":
                    self.height = (kwargs[kw])
                if kw == "x":
                    self.x = (kwargs[kw])
                if kw == "y":
                    self.y = (kwargs[kw])

    def to_dictionary(self):
        """returns dictionary representation of a Rectangle"""
        dict_rep = {}
        dict_rep["id"] = self.id
        dict_rep["width"] = self.width
        dict_rep["height"] = self.height
        dict_rep["x"] = self.x
        dict_rep["y"] = self.y
        return dict_rep
