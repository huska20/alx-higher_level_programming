#!/usr/bin/python3
"""Defines a function for adding files."""
def append_write(filename="", text=""):
    """Annexes a string to the furthest limit of an UTF8 text record.
    Args:
        filename (str): the file's name that needs to be added.
        str: text the text that will be added to the file.
    Returns:
        the added number of characters.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
