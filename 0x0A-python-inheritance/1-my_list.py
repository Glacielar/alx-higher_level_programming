#!/usr/bin/python3
"""Defines an inherited class list MyList"""

class Mylist(list):
"""Implements sorting for built-in list class."""

     def print_sorted(self):
       """Print a list in sorted ascending order."""
      print(sorted(self))
