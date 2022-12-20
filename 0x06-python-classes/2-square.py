#!/usr/bin/python3
"""Definition.
Defines a square
"""


class Square:
    """A square representation
    """
    def __init__(self, size=0):
        """Initialize a square
        Args:
            size (`int`): The size of the ``Square``.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._Square__size = size
