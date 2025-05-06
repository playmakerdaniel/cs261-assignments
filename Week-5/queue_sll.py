# Name: Daniel Burrows
# OSU Email: burrdani@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3 Linked List and ADT Implementation
# Due Date: 05/05/2025
# Description: This assignment comprises of 5 parts. In the first part, you will complete the implementation of a Singly Linked List data structure.
# In part 2, you will implement the Stack ADT using your Dynamic Array from Assignment 2. For part 3, you will implement the Queue ADT using your Static Array from Assignment 1. For parts 4 and 5, you will again implement the Stack and Queue ADTs, but by using the Singly Linked Nodes


from SLNode import SLNode


class QueueException(Exception):
    """
    Custom exception to be used by Queue class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Queue:
    def __init__(self) -> None:
        """
        Initialize new queue with head and tail nodes
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = None
        self._tail = None

    def __str__(self):
        """
        Return content of queue in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'QUEUE ['
        if not self.is_empty():
            node = self._head
            out = out + str(node.value)
            node = node.next
            while node:
                out = out + ' -> ' + str(node.value)
                node = node.next
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the queue is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._head is None

    def size(self) -> int:
        """
        Return number of elements currently in the queue
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        node = self._head
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    # -----------------------------------------------------------------------

    def enqueue(self, value: object) -> None:
        new_node = SLNode(value)

        # If queue is empty, head and tail both point to the new node
        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            # Attach to the tail and move the tail pointer
            self._tail.next = new_node
            self._tail = new_node

    def dequeue(self) -> object:
        if self.is_empty():
            raise QueueException()

        value = self._head.value
        self._head = self._head.next

        # If queue is now empty, reset tail to None
        if self._head is None:
            self._tail = None

        return value

    def front(self) -> object:
        if self.is_empty():
            raise QueueException()
        return self._head.value


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# enqueue example 1")
    q = Queue()
    print(q)
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)

    print("\n# dequeue example 1")
    q = Queue()
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)
    for i in range(6):
        try:
            print(q.dequeue())
        except Exception as e:
            print("No elements in queue", type(e))

    print('\n#front example 1')
    q = Queue()
    print(q)
    for value in ['A', 'B', 'C', 'D']:
        try:
            print(q.front())
        except Exception as e:
            print("No elements in queue", type(e))
        q.enqueue(value)
    print(q)
