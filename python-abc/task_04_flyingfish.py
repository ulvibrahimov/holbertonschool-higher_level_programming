#!/usr/bin/env python3
"""Module that demonstrates multiple inheritance."""


class Fish:
    """A simple Fish class."""

    def swim(self):
        """Prints the swimming action of a fish."""
        print("The fish is swimming")

    def habitat(self):
        """Prints the habitat of a fish."""
        print("The fish lives in water")


class Bird:
    """A simple Bird class."""

    def fly(self):
        """Prints the flying action of a bird."""
        print("The bird is flying")

    def habitat(self):
        """Prints the habitat of a bird."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """A FlyingFish class that inherits from both Fish and Bird."""

    def fly(self):
        """Overrides the fly method for a flying fish."""
        print("The flying fish is soaring!")

    def swim(self):
        """Overrides the swim method for a flying fish."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Overrides the habitat method for a flying fish."""
        print("The flying fish lives both in water and the sky!")
