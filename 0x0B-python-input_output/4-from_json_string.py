#!/usr/bin/python3
# 6-from_json_string.py
"""Defines a function that converts JSON to an object."""

import json
def from_json_string(my_str):
    """Return the Python object portrayal of a JSON string."""
    return json.loads(my_str)
