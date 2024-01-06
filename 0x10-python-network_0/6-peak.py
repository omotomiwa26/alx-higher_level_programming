#!/usr/bin/python3
"""
    This function finds a peak in a list of
    unsorted integers.
"""


def find_peak(list_of_integers):
    """
        Args:
        - list_of_integers: A list of unsorted integers.

        Returns:
        - A peak element from the list.
    """
    if not list_of_integers:
        return None

    elif list_of_integers:
        list_of_integers.sort(reverse=True)
        return list_of_integers[0]
