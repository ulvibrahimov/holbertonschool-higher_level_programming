#!/usr/bin/env python3
"""Module that defines a VerboseList inheriting from the built-in list."""


class VerboseList(list):
    """A list subclass that prints a message whenever it is modified."""

    def append(self, item):
        """Appends an item to the list and prints a notification."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """Extends the list with an iterable and prints a notification."""
        # Calculate the length before extending in case iterable is a generator
        count = len(iterable)
        super().extend(iterable)
        print("Extended the list with [{}] items.".format(count))

    def remove(self, item):
        """Removes an item from the list and prints a notification."""
        # Call super().remove() first to catch ValueError if item doesn't exist
        super().remove(item)
        print("Removed [{}] from the list.".format(item))

    def pop(self, index=-1):
        """Pops an item from the list and prints a notification."""
        # Call super().pop() first to catch IndexError if list is empty
        item = super().pop(index)
        print("Popped [{}] from the list.".format(item))
        return item
