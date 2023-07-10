#!/usr/bin/python3
"""Defines lookup function for an object attribute."""

def lookup(obj):
    """Return a list of an object's available attributes."""
    return (dir(obj))
