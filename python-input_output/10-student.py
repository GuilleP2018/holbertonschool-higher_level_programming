#!/usr/bin/python3
"""Module for Student class."""


class Student:
    """Class for student."""

    def __init__(self, first_name, last_name, age):
        """Constructor."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Method for to_json."""
        if attrs is not None:
            new_dict = {}
            for i in attrs:
                if str(i) == "first_name":
                    new_dict[i] = self.first_name
                elif str(i) == "last_name":
                    new_dict[i] = self.last_name
                elif str(i) == "age":
                    new_dict[i] = self.age
            return new_dict
        else:
            return self.__dict__
