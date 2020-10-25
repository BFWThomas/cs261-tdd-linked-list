# LinkedList: A doubly-linked list.
# Bonus: Has an insert_in_order that, when used, keeps the values of
#        each node in ascending order.
# Implement as many operations as possible with recursion.
# If you can't figure it out recursively, use a loop. (But then refactor
# your implementation into a recursive one!)
# Your implementation should pass the tests in test_sorted_list.py.
# Brian F Thomas

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
        return self._last.next == self and self.value is None

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
        Appends a new node to end of linked list
        """
        self._last.next = new_node
        new_node.next = self
        new_node.prev = self._last
        self.prev = new_node
        self._last = new_node

    def delete(self):
        """
        Removes the node from the linked list
        """
        self.next.prev = self.prev
        self.prev.next = self.next

    def insert(self, new_node):
        """
        Inserts a new node to the linked list
        """
        new_node.prev = self
        new_node.next = self.next
        self.next.prev = new_node
        self.next = new_node

    def insert_in_order(self, new_node):
        """
        Inserts a new node while maintaining list order
        """
        if self.next.value is None:  # If list is empty, just append
            self.append(new_node)
            return
        elif self.next.value > new_node.value:  # If next node in list has larger value, append here
            self.insert(new_node)
            return
        # if next node in list has smaller value, call method on next node
        return self.next.insert_in_order(new_node)

    def at(self, node):
        """
        Returns the node in the Nth position of the linked list
        Must be called on the sentinel node
        """
        if node == 0:
            return self
        else:
            return self.next.at(node-1)

    def search(self, val):
        """
        Returns the node that contains search value or None if doesn't exist in linked list
        """
        if self.value == val:
            return self
        else:
            if self == self._last:
                return None
            else:
                return self.next.search(val)