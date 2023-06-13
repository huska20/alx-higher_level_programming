#!/usr/bin/python3
"""Defines a class-to-JSON function in Python."""
def class_to_json(obj):
    """Return the word reference represntation of a basic information structure."""
    return obj.__dict__
