def insertion_Sort(A, order):
    """
    Sorts list of a comparable element based on order preference given
    \n Runs in O(n^2), quadratic time

    :param A: Sequence to be sorted
    :param order: Order to sort list in
    :return: Sorted list
    """

    for i in range(1, len(A)):  # iterate through list, from 1 to n - 1
        curr = A[i]  # current element to be inserted
        j = i  # get index for current
        if order == 'ascending':
            while j > 0 and A[j - 1] > curr:  # compare elements to left of current index for correct position
                A[j] = A[j - 1]  # swap element at current index with element directly to the left
                j -= 1  # move to the left of swapped element (j - 2)
            A[j] = curr  # current element is now in correct position

        if order == 'descending':
            while j > 0 and A[j - 1] < curr:  # compare elements to left of current index for correct position
                A[j] = A[j - 1]  # swap element at current index with element directly to the left
                j -= 1  # move to the left of swapped element (j - 2)
            A[j] = curr  # current element is now in correct position
