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
        \n Runs in constant, O(1) time
        :return: True if the array is empty, False otherwise
        """
        return self._n == 0

    def __getitem__(self, k):
        """
        Accesses the element at a specific index in the array
        \n Runs in constant time
        :param k: Index of item which is to be retrieved
        :return: Element at specified index
        """
        if not 0 <= k < self._n:  # Conditional to check out if index is out of bounds
            raise IndexError('Invalid index')
        return self._A[k]

    def __setitem__(self, k, element):
        """
        Updates the value of an element at given index k
        \n Runs in constant, O(1) time
        :param k: Index in which element is to be updated
        :param element: Element which index k is to be updated with
        """
        if not 0 <= k < self._n:  # Conditional to check if index is out of bounds
            raise IndexError('Invalid index')
        self._A[k] = element

    def __str__(self):
        """
        Returns a string representation of the dynamic array
        \n Runs in constant, O(1) time
        :return: String representation of the Array
        """
        elements = [str(self._A[i]) for i in range(self._n)]
        return "[" + ", ".join(elements) + "]"

    def append(self, element):
        """
        Add an object to the end of the array
        \n Runs in amortized constant, O(1) time
        :param element: Element to be added to the end of the array
        """

        self._check_Resize()

        self._A[self._n] = element
        self._n += 1  # update the number of elements currently occupying the array

    def pop(self, k=-1):
        """
        Removes and returns the last element from this array if no argument is given, otherwise returns element at
        position specified by k
        \n Performs a shrinking operation when size is 1/4 of capacity, resizing
        to half of current size
        \n Runs in amortized constant, O(1) time
        :return: Last item in the list, or element at index K
        """

        if self.is_empty():  # check if array is empty
            raise Exception('Array is empty')

        if k == -1:  # Checks whether argument was passed, if not method implements pop() method

            value = self._A[self._n - 1]
            self._A[self._n - 1] = None  # Garbage collect
            self._n -= 1  # update size of list to reflect removal of element

            return value
        else:
            if not 0 <= k < self._n:  # Checks whether given index is out of bounds
                raise IndexError('Invalid index')

            value = self._A[k]

            for i in range(k, self._n - 1):  # Shift elements left to fill "gap" left by removed element at index k
                self._A[i] = self._A[i + 1]

            self._A[self._n - 1] = None  # Garbage collect
            self._n -= 1  # update size of list to reflect removal of element

            self._check_Resize()

            return value

    def remove(self, element):
        """
        Removes the first occurrence of the specified element of the array, if exists
        \n Runs in linear, O(n) time
        :param element: Element to be removed
        """
        for i in range(self._n):  # iterate through entire list, searching for first occurrence of element
            if self._A[i] == element:

                for j in range(i, self._n - 1):  # Shift elements left to fill "gap" left by removal of element
                    self._A[j] = self._A[j + 1]

                self._A[self._n - 1] = None  # Garbage collect
                self._n -= 1  # update size of list to reflect removal of element

                self._check_Resize()

                return

        raise ValueError('Value not found')

    def removeAll(self, element):
        """
        Removes all occurrences of the specified element of the array, if exists
        Runs in quadratic, O(n^2) time
        :param element: Element to be removed
        """
        count = 0  # counter to keep track of the number of occurrences found

        for i in range(self._n):   # iterate through the entire list, searching for all occurrences of element
            if self._A[i] == element:
                count += 1

                for j in range(i, self._n - 1):  # Shift element left to fill "gap" left by removal of elements
                    self._A[j] = self._A[j + 1]

                self._A[self._n - 1] = None  # Garbage collect

        if count == 0:
            raise ValueError('Value not found')

        self._n -= count  # update size of list to reflect removal of element
        self._check_Resize()

    def _check_Resize(self):
        """
        Private utility method to handle checking whether resize operation is needed, shrinking or expanding if needed
        """
        if self._n == self._SHRINK_FACTOR * self._capacity:  # Check whether array is 1/4 of capacity, resize to half
            self._resize(self._capacity // 2)  # calling resize method to half current capacity of array\

        if self._n == self._capacity:  # Check whether array capacity has been reached
            self._resize(self._capacity * self._GROWTH_FACTOR)  # calling resize method to double capacity

    def _resize(self, cap):
        """
        Private utility method to handle the internal resizing of low-level array
        :param c: New capacity of the array to be created
        :return: Newly resized array
        """
        newArray = self._make_array(cap)  # creates a new (bigger) array

        for i in range(self._n):  # iterate over current array and copy over elements to new array
            newArray[i] = self._A[i]

        self._A = newArray  # updating the underlying array to now reference newly created (larger) array
        self._capacity = cap  # update capacity of array

    def _make_array(self, cap):
        """
        Private utility method to handle creating the low-level array
        :param c: Capacity of array
        :return: Returns new array with specified capacity
        """
        return (cap * ctypes.py_object)()
