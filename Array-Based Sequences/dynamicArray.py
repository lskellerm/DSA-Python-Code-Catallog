import ctypes

from Sorting.InsertionSort import insertion_Sort


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

    def __getitem__(self, k):
        """
        Accesses the element at a specific index in the array or a range of indices in the array
        \n Runs in O(1), when single index is given, or O(k) when range is given, where k is length of slice
        :param k: Index of item which is to be retrieved, or slice object indicating items to be retrieved
        :return: Element at specified index, or new DynamicArray with the specified slice elements
        """
        if isinstance(k, slice):  # checks whether value given is a slice object
            start, stop, step = k.indices(self._n)  # get the start, stop, and step values from the slice
            sliced_array = DynamicArray(stop - start)  # create new dynamicArray object for sliced elements
            sliced_array._set_n(stop - start)  # set number of elements to allow indexing in new dynamicArray

            for i in range(start, stop, step):  # iterate through array with specified sliced range
                sliced_array[i - start] = self._A[i]  # copy sliced elements into the new dynamicArray

            return sliced_array

        elif not 0 <= k < self._n:  # checks if index is out of bounds
            raise IndexError('Invalid index')
        else:
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
        \n Runs in constant, O(n) time
        :return: String representation of the Array
        """
        elements = [str(self._A[i]) for i in range(self._n)]
        return "[" + ", ".join(elements) + "]"

    def __add__(self, other_array):
        """
        Concatenates two arrays together, and returns result as new DynamicArray
        Runs in O(n) time, linear where n is the total number of elements in both arrays
        :param other_array: Array to be concatenated to current array
        :return Concatenated DynamicArray
        """
        new_Array_Size = len(other_array) + self._n  # obtain the size of the new array
        newArray = DynamicArray(new_Array_Size)  # create a new dynamic array
        newArray._set_n(new_Array_Size)  # set number of elements to allow indexing in new dynamicArray

        for i in range(self._n):  # iterate through first array and copy elements to new array
            newArray[i] = self._A[i]

        for i in range(len(other_array)):  # iterate through second array and copy elements to new array
            newArray[self._n + i] = other_array[i]

        return newArray

    def is_empty(self):
        """
        Checks if the array is empty
        \n Runs in constant, O(1) time
        :return: True if the array is empty, False otherwise
        """
        return self._n == 0

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
        Runs in linear, O(n) time, achieving this using pointers rather than a nested loop
        :param element: Element to be removed
        """
        count = 0  # counter to keep track of the number of elements needing to be removed
        non_Matching_index = 0  # pointer to track index of non-matching element

        for i in range(self._n):  # iterate through the entire list, searching for all occurrences of element

            if self._A[i] != element:  # check if current element does not match target element
                self._A[non_Matching_index] = self._A[i]  # store non-matching element at current
                non_Matching_index += 1  # increment pointer

        count = self._n - non_Matching_index  # update the number of elements removed

        for i in range(non_Matching_index, self._n - 1):  # iterate through list and garbage collect
            self._A[i] = None

        self._n -= count  # update size of list to reflect removal of element
        self._check_Resize()  # perform resizing operation if necessary

        if count == 0:
            raise ValueError('Value not found')

    def insert(self, index, element):
        """
        Inserts specified element at the given index
        \n Runs in linear, O(n) time
        :param index: Index where specified element is to be inserted
        :param element: Element to be inserted
        """
        if not 0 < index < self._n:  # Checks whether given index is out of bounds
            raise IndexError('Invalid index')

        self._check_Resize()  # perform resizing operation if necessary

        for i in range(self._n, index, -1):  # iterate through list and shift elements after index right
            self._A[i] = self._A[i - 1]

        self._A[index] = element  # insert newest element in desired position
        self._n += 1  # update the size of array

    def clear(self):
        """
        Removes all elements from the array
        \n Runs in constant, O(1) time
        """
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def index(self, element):
        """
        Returns the index of the first occurrence of the specified element
        \n Runs in linear, O(n) time
        :param element: Element to search for
        :return: Index of the first occurrence of the specified element, -1 if not found
        """

        for i in range(self._n):  # iterate through array, searching for first occurrence of element
            if self._A[i] == element:
                return i

        return -1

    def count(self, element):
        """
        Counts the number of occurrences of a specified element in the array
        \n Runs in linear, O(n)  time
        :param element: Element to be searched for
        :return: Number of elements with the specified value
        """
        count = 0

        for i in range(self._n):  # iterate through array, counting occurrences of specified element
            if self._A[i] == element:
                count += 1

        return count

    def reverse(self):
        """
        Reverses the order of elements in the array
        \n Runs in linear, O(n) time.
        Utilizes in-place reversal, and the two-pointer approach
        """
        start = 0  # start pointer, for the first element
        end = self._n - 1  # end pointer, for the last element

        while start < end:  # iterate through array until they meet or cross, meaning start > end
            self._A[start], self._A[end] = self._A[end], self._A[start]  # swap the elements at start & end position
            # utilizing tuple unpacking

            #  increment/decrement both pointers
            start += 1
            end -= 1

    def extend(self, other_array):
        """
        Appends the elements from another array to the current array
        \n Runs in O(m) time, where m is length of the other array
        :param other_array: Array to be appended to current array
        """
        array_Size = len(other_array)
        if array_Size + self._n > self._capacity:  # check if current capacity is enough for appending other array
            self._resize(self._n + array_Size)  # resize array to accommodate resulting array size

        for i in range(array_Size):  # iterate through other array and append each element to the current array
            self._A[self._n] = other_array[i]  # assigning element to the next available position
            self._n += 1  # update size of array

    def copy(self):
        """
        Returns a new dynamicArray object that is a copy of the current array
        \n Runs in O(n), linear time
        :return: A copy of the specified array
        """
        new_Array = DynamicArray(self._capacity)  # New instance of the dynamicArray object
        new_Array._set_n(self._n)  # set number of elements to allow indexing in new dynamicArray

        for i in range(self._n):  # iterate through current array
            new_Array[i] = self._A[i]

        return new_Array

    def sort(self, order='ascending'):
        """
        Sorts the elements in the dynamicArray, ascending order if none is given
        \n Runs in O(n^2), quadratic time, implemented using InsertionSort algorithm
        :param order: Order in which array is sorted, default is ascending
        :return: Sorted dynamic array
        """
        insertion_Sort(self, order)

    def _check_Resize(self):
        """
        Private utility method to handle checking whether resize operation is needed, shrinking or expanding if needed
        """
        if self._n == self._SHRINK_FACTOR * self._capacity:  # Check whether array is 1/4 of capacity, resize to half
            self._resize(self._capacity // 2)  # calling resize method to half current capacity of array

        if self._n == self._capacity:  # Check whether array capacity has been reached
            self._resize(self._capacity * self._GROWTH_FACTOR)  # calling resize method to double capacity

    def _resize(self, cap):
        """
        Private utility method to handle the internal resizing of low-level array
        :param c: New capacity of the array to be created
        :return: Newly resized array
        """
        new_Array = self._make_array(cap)  # creates a new (bigger) array

        for i in range(self._n):  # iterate over current array and copy over elements to new array
            new_Array[i] = self._A[i]

        self._A = new_Array  # updating the underlying array to now reference newly created (larger) array
        self._capacity = cap  # update capacity of array

    def _set_n(self, numOfElements):
        """
        Private utility method to only be used by the __get__, __add__ and copy function to update the number of
        elements in the newly created array from concatenation operation purposes
        :param numOfElements: Number of elements
        """
        self._n = numOfElements

    def _make_array(self, cap):
        """
        Private utility method to handle creating the low-level array
        :param c: Capacity of array
        :return: Returns new array with specified capacity
        """
        return (cap * ctypes.py_object)()
