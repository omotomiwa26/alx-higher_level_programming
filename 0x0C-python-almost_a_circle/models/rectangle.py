#!/usr/bin/python3
"""
This module defines the class Rectangle
that inherits from base
"""


from models.base import Base


class Rectangle(Base):
    """
    Defining and initialisng the Rectangle class
    with the private instance attributes.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialise rectangle constructor
            Args:
                width.
                height.
        """
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """
        Define and return the area of
        the rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """
        Define and prints to stdout with
        the character '#' and then update
        to take care of 'x' and 'y'
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def __str__(self):
        """
        Define and print
        formatted string
        """
        return (F'[Rectangle] ({self.id}) {self.__x}/{self.__y} '
                F'- {self.__width}/{self.__height}')
