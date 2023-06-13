#!/usr/bin/python3
"""Defines a student in a class."""

class Student:
    """Address a student."""
    def __init__(self, first_name, last_name, age):
        """
        Set up a brand-new student.
        Args:
            (str) first_name: The principal name of the understudy.
            (String): last_name the student's last name.
            age (int): The age of the understudy.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Obtain a dictionary image of the student."""
        return self.
