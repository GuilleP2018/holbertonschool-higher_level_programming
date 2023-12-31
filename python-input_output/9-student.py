#!/usr/bin/python3
"""Module for Student class."""


class Student:
    """Class for student."""

    def __init__(self, first_name, last_name, age):
        """Constructor."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Method for to_json."""
        return self.__dict__
