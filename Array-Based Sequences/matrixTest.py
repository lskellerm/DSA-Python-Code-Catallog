import unittest
from matrix import Matrix


class MatrixTest(unittest.TestCase):
    def setUp(self):
        self.matrix = Matrix(3, 3)
