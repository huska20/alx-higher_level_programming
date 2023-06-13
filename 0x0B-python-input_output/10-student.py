#!/usr/bin/python3
"""Characterizes a class Student."""
class Student:
    """Speak for a student."""
        def __init__(self, first_name, last_name, age):
            """
            Set up a brand-new student.
        Args:
            (str) first_name: The main name of the understudy.
            (String): last_name the student's last name.
            age in units: how old the student is.
        """
         self.first_name = first_name
        self.last_name = last_name
        self.age = age
        def to_json(self, attrs=None):
            """
            Get an image of the student from a dictionary.
        If attrs is a list of strings, only the attributes in the list are represented.
        Args:
            attributes (list): Discretionary) The characteristics to address.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
