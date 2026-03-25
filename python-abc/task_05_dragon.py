#!/usr/bin/env python3
"""Module that demonstrates the use of Mixins."""


class SwimMixin:
    """A mixin that provides swimming capability."""

    def swim(self):
        """Prints a swimming message."""
        print("The creature swims!")


class FlyMixin:
    """A mixin that provides flying capability."""

    def fly(self):
        """Prints a flying message."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A Dragon class that mixes in swimming and flying."""

    def roar(self):
        """Prints a roaring message."""
        print("The dragon roars!")
