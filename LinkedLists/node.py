class Node:
    def __init__(self, data):
        """
        Constructor for a lightweight node object, which creates an empty Node
        :param data: The data value for this node object
        """
        self.data = data # value/data stored in the node
        self._next = None # Reference to the next node in a linked list

    def get_next(self):
        """
        Getter to obtain the next node of calling node, implemented to enforce strict
        encapsulation

        :return: The next node pointed to by the _next variable
        """
        return self._next

    def set_next(self, next_node):
        """
        Setter which sets the next node of the calling node in a linked list, implemented to
        enforce strict encapsulation

        :param next_node: The node which is to be set as the next node
        """
        self._next = next_node



