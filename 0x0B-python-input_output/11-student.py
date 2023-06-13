#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """
        Set up a brand-new student.
        Args:
            (str) first_name: the student's first name.
            last_name (str): The last name of the understudy.
            age in units: how old the student is.
        """
         self.first_name = first_name
        self.last_name = last_name
        self.age = age
        def to_json(self, attrs=None):
            """
            Get an image of the student from a dictionary.
        On the off chance that attrs is a rundown of strings, addresses just those credits
        remembered for the rundown.
        Args:
            attrs (list): ( Discretionary) The traits to address.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace the Student in every way.
        Args:
            json (dict): the key-value pairs that can be used to replace attributes.
        """
        for k, v in json.items():
            setattr(self, k, v)
