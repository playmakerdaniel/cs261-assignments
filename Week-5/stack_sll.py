# Name: Daniel Burrows
# OSU Email: burrdani@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3 Linked List and ADT Implementation
# Due Date: 05/05/2025
# Description: This assignment comprises of 5 parts. In the first part, you will complete the implementation of a Singly Linked List data structure.
# In part 2, you will implement the Stack ADT using your Dynamic Array from Assignment 2. For part 3, you will implement the Queue ADT using your Static Array from Assignment 1. For parts 4 and 5, you will again implement the Stack and Queue ADTs, but by using the Singly Linked Nodes


from SLNode import SLNode


class StackException(Exception):
    """
    Custom exception to be used by Stack class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Stack:
    def __init__(self) -> None:
        """
        Initialize new stack with head node
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = None

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'STACK ['
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
        Return True is the stack is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._head is None

    def size(self) -> int:
        """
        Return number of elements currently in the stack
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        node = self._head
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    # -----------------------------------------------------------------------

    def push(self, value: object) -> None:
        # Create a new node pointing to the current top
        new_node = SLNode(value)
        new_node.next = self._head

        # Update head to point to the new top node
        self._head = new_node

    def pop(self) -> object:
        if self.is_empty():
            raise StackException()

            # Grab the top value and move head to the next node
        value = self._head.value
        self._head = self._head.next
        return value

    def top(self) -> object:
        if self.is_empty():
            raise StackException()
        return self._head.value


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# push example 1")
    s = Stack()
    print(s)
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    print(s)

    print("\n# pop example 1")
    s = Stack()
    try:
        print(s.pop())
    except Exception as e:
        print("Exception:", type(e))
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    for i in range(6):
        try:
            print(s.pop())
        except Exception as e:
            print("Exception:", type(e))

    print("\n# top example 1")
    s = Stack()
    try:
        s.top()
    except Exception as e:
        print("No elements in stack", type(e))
    s.push(10)
    s.push(20)
    print(s)
    print(s.top())
    print(s.top())
    print(s)
