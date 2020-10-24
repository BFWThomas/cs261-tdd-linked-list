# LinkedList: A doubly-linked list.
# Bonus: Has an insert_in_order that, when used, keeps the values of
#        each node in ascending order.
# Implement as many operations as possible with recursion.
# If you can't figure it out recursively, use a loop. (But then refactor
# your implementation into a recursive one!)
# Your implementation should pass the tests in test_sorted_list.py.
# YOUR NAME

class LinkedList:

    class Node:
        """
        Used to create nodes for the Linked List
        """

    def __init__(self, value=None):
        self.value = value
        self.next = self
        self.prev = self
        self._last = self

    def is_sentinel(self):
        """
        Returns if list node has a value of 'None'
        """
        return self.value is None

    def is_empty(self):
        """
        Returns if list contains anything
        """
        return self.next == self and self.prev == self

    def is_last(self):
        """
        Return if node is the last
        """
        return self._last == self

    def last(self):
        """
        Returns the last node
        """
        return self._last

    def append(self, new_node):
        """
        Appends a new node
        """
        self.next = new_node
        new_node.prev = self
        new_node.next = self
        self.prev = new_node