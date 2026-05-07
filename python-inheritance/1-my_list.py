#!/usr/bin/python3
"""Module that provides a MyList class inheriting from list."""


class MyList(list):
    """A class that inherits from list and adds a print_sorted method."""

    def print_sorted(self):
        """Prints the list in ascending sorted order without modifying the original."""
        print(sorted(self))
