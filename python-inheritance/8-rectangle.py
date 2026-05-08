#!/usr/bin/python3
"""Module that provides a Rectangle class inheriting from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A Rectangle class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initializes a Rectangle with a validated private width and height.

        Args:
            width: The width of the rectangle, must be a positive integer.
            height: The height of the rectangle, must be a positive integer.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
