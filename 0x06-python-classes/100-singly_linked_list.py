#!/usr/bin/python3
"""singly linked list"""


class Node:
    """node defined"""

    def __init__(self, data, next_node=None):
        """node initialization with instance variables"""

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """gets data attribte"""

        return (self.__data)

    @data.setter
    def data(self, value):
        """sets data attribte"""

        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """get next_node attribute
        Returns: next node
        """

        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """set value next node"""

        if (value is not None and not isinstance(value, Node)):
            raise TypeError('next_node must be a Node object')

        self.__next_node = value


class SinglyLinkedList:
    """singly linked list definition"""

    def __init__(self):
        """singly linked list initialization"""

        self.head = None

    def __str__(self):
        """make list printable"""

        printsll = ""
        temp = self.head
        while temp:
            printsll += str(temp.data) + "\n"
            temp = temp.next_node
        return printsll[:-1]

    def sorted_insert(self, value):
        """insert in a sorted order
        Args:
            value: node's value
        """
        new = Node(value)
        if not self.head:
            self.head = new
            return
        if value < self.head.data:
            new.next_node = self.head
            self.head = new
            return
        temp = self.head
        while temp.next_node and temp.next_node.data < value:
            temp = temp.next_node
        if temp.next_node:
            new.next_node = temp.next_node
        temp.next_node = new
