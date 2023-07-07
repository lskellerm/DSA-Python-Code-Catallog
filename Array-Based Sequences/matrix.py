from dynamicArray import DynamicArray


class Matrix:
    """A two-dimensional array implemented using a dynamic Array of dynamic Arrays

       This class supports common Matrix operations
    """

    def __init__(self, rows, cols):
        """
        Constructor for a Matrix object which creates an empty Matrix with the specified dimensions
        :param rows: Number of rows for the Matrix
        :param cols: Number of cols for the Matrix
        """
        self.rows = rows
        self.column = cols
        self.data = DynamicArray(rows)  # Use DynamicArray to store the matrix data

        for _ in range(rows):
            self.data.append(DynamicArray(cols))  # Use DynamicArray for each row in the matrix

