#!/usr/bin/python3
"""Defines a locked class."""
class LockedClass:
    """
    Make it impossible for the user to create new LockedClass attributes for anything other than attributes called
    'first_name'.
    """

    __slots__ = ["first_name"]
