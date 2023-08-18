from node import Node


class LinkedList:
    """
        A singularly linked list, utilizing the Node ADT to implement Node functionalities

        This implementation uses the Head and Tail pointers to denote the first node in the list and the last node in
        the list, respectively.

        This class supports basic and some additional linked list functionality.

        Tested using the unit tests in linkedListTest.py
    """

    def __init__(self):
        """
            Constructor for LinkedList object which creates an initially empty LinkedList
        """
        self._size = 0
        self.head = None
        self.tail = None

    def __len__(self):
        """
        Returns the number of elements stored in the LinkedIst
        \n Runs in constant, O(1) time
        :return: The number of nodes in the LinkedList
        """
        return self._size

    def is_Empty(self):
        """
        Checks if the Linked List is empty
        \n Runs in constant, O(1) time
        :return: True if the Linked is empty, False otherwise
        :raises
        """
        return self._size == 0

    def value_At(self, index):
        """
        Returns the value at the nth node (0-indexed)
        \n Runs in linear, O(n) time, where n is the number of nodes in the linked List
        :param index: The index of the item to retrieve
        :return: The value of the node at the given index
        :raises IndexError if the index is out of range or if the list is empty
        """

        # Check if Linked List is empty
        if self.is_Empty():
            raise IndexError('Linked List is empty')

        # Check for invalid index
        if index < 0 or index > self._size - 1:
            raise IndexError('Index out of range')

        curr = self.head

        # Traverse Linked list to desired index
        for _ in range(index):
            curr = curr.get_next()

        # Return the value of the node at the given index
        return curr.data

    def push_Front(self, value):
        """
        Adds a new with the given value to the front of the linked list (Head)
        \n Runs in constant, O(1) time
        :param value: Value of the new node
        """
        new_Node = Node(value)  # Creates a new node with the provided value
        new_Node.set_next(self.head)  # Sets the new nodes next pointer to point to current head

        self.head = new_Node  # Update the head to point to the new node

        if self.is_Empty():  # Checks if the linked list is initially empty
            self.tail = new_Node  # Set tail to new node, now Head and Tail reference same node

        self._size += 1  # Increment the size of linked list

    def pop_Front(self):
        """
        Removes the front node from the linked list and returns its value
        \n Runs in constant, O(1) time.

        :return: The value from the remove front node (Head)
        :raises Exception: If the Linked List is empty
        """

        if self.is_Empty():  # Checks whether Linked List is empty
            raise Exception("Linked List is empty")

        popped_Value = self.head.data  # Retrieve the value of the current head

        self.head = self.head.get_next()  # Update the head to next node

        if self.head is None:  # If the list is now empty, update the tail to None
            self.tail = None

        self._size -= 1  # Decrement the size

        return popped_Value  # Return the value of front popped_node
