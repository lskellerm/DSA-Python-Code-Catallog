import ctypes


class DynamicArray:
    """A dynamic array class similar to a Python list with automatic resizing capabilities

       This class supports common list/array operations
    """

    def __init__(self, cap=1):
        """
        Constructor for dynamic array object which creates an empty array

        :param cap: Capacity of Array
        """
        self._n = 0  # counts actual number of elements present in the array
        self._capacity = cap  # array capacity, default of 1
        self._A = self._make_array(self._capacity)  # low-level array
        self._GROWTH_FACTOR = 2  # Growth factor for resize operation
        self._SHRINK_FACTOR = 0.25  # Shrink factor for resize operation

    def __len__(self):
        """
        Returns the number of elements stored in the array
        \n Runs in constant, O(1) time
        :return: The length of the array
        """
        return self._n

    def is_empty(self):
        """
        Checks if the array is empty
        :return: True or False, depending on if array is empty or not
        """


    def _make_array(self, c):
        """
        Private utility method to handle creating a low-level array
        :param c: Capacity of array
        :return: Returns new array with specified capacity
        """
        return (c * ctypes.py_object)()
