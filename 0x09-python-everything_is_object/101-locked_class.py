#!/usr/bin/python3
"""A module with a locked class"""


class LockedClass:
    """
    Defines the ONLY allowed instance attribute called first_name
    """

    __slots__ = ["first_name"]
