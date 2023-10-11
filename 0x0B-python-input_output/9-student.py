#!/usr/bin/python3
"""
This module initializes a Student instance
with first_name, last_name, and age.
"""
class Student:
    """
    Defining and initialising the student class
    """
    def __init__(self, first_name, last_name, age):
        """
        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self):
        """
        Retrieve a dictionary representation
        of a Student instance.

        Returns:
            dict: A dictionary containing the attributes 
            of the Student instance.
        """
        return self.__dict__
