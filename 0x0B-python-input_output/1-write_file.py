#!/usr/bin/python3
"Defines a function for writing files."

def write_file(filename="", text=""):
    """
    Copy a string to a UTF-8 text file.
    Args:
        filename (str): the file's name to be written.
        str: text the written text for the file.
    Returns:
        the total number of written characters.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
