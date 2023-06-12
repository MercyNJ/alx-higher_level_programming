#!/usr/bin/python3
"""Defining a class MyInt inheriting from int."""


class MyInt(int):
    """Invert int operators == and != like a rebel!"""

    def __eq__(self, other):
        """Override == opeartor with != behavior."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override != operator with == operator"""
        return super().__eq__(other)
