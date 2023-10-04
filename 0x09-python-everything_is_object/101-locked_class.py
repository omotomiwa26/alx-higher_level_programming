#!/usr/bin/python3
"""
    This file defines a class LockedClass
"""


class LockedClass:
    """
        This function defines a class LockedClass with no class or
        object attribute,
        that prevents the user from dynamically creating
        new instance attributes,
        except if the new instance attribute is called first_name.
    """
    def __setattr__(self, name, value):
        """
            intiializing the set attributes for the class
        """
        if name == "first_name":
            super().__setattr__(name, value)
        else:
            raise AttrributeError("Ooops!!...set only first_name")
