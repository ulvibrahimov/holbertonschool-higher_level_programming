#!/usr/bin/env python3
"""Module that defines a CountedIterator class."""


class CountedIterator:
    """An iterator that keeps track of the number of items yielded."""

    def __init__(self, some_iterable):
        """Initializes the iterator and the counter.
        
        Args:
            some_iterable: An iterable object to iterate over.
        """
        self.iterator = iter(some_iterable)
        self.count = 0

    def get_count(self):
        """Returns the current count of iterated items."""
        return self.count

    def __next__(self):
        """Returns the next item from the iterator and increments the count."""
        # next() will naturally raise StopIteration when empty
        item = next(self.iterator)
        self.count += 1
        return item
