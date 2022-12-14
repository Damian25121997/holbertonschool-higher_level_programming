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

    @property
    def size(self):
        return self.__width

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    def update(self, *args, **kwargs):
        """Updates attributes"""

        if args is not None and len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """Return the dictionary representation of a Square"""

        dic = {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
        return dic
