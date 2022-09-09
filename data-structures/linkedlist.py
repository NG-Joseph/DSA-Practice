class Node:
    """
    Object for storing a single node of a linked list.
    It models two attributes - Data and the next node in the list
    """
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data


class LinkedList:
    """
    Singly linked list
    :returns the number of nodes in a list. Takes O(n) time.
    """
    def __init__(self):
        self.head = None

    def is_empty(self):
        return None == self.head

    def size(self):
        curr = self.head
        count = 0

        while curr:
            count += 1
            curr = curr.next_node
        return count


N1 = Node(10)
