#!/usr/bin/python3
"""
This module defines the class Rectangle
that inherits from base
"""


from models.base import Base
import json as j


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
        return self.__height

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

    def update(self, *args, **kwargs):
        """
         Update the attributes of the Rectangle
         using both *args and **kwargs.
        Arguments:
        - args: A tuple of arguments in the following order:
            1. id attribute
            2. width attribute
            3. height attribute
            4. x attribute
            5. y attribute
        - kwargs: A dictionary where each key
        represents an attribute to update.
        """
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Return a dictionary representation of the Rectangle.
        Returns:
        - A dictionary with the following keys:
            - 'id': The id attribute of the Rectangle
            - 'width': The width attribute of the Rectangle
            - 'height': The height attribute of the Rectangle
            - 'x': The x attribute of the Rectangle
            - 'y': The y attribute of the Rectangle
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
