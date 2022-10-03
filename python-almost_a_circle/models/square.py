#!/usr/bin/python3
"""Define a class Square"""


from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """The class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a Square instance"""

        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return a string representation of a square"""

        string = "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.size)
        return string
