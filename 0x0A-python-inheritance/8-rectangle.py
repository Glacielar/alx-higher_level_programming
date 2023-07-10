#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle:
"""Represent a Rectangle using BaseGeometry."""

def __init__(self, width, height):
       """ Intialize a new Rectangle.

      Args:
        width(int): Width of the Rectangle
        height(int): Height od the Rectangle
      """
      self.integer_validator("width", width)
      self.__width = width
      self.integer_validator("height", height)
      self.__height = height
