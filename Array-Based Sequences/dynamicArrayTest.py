import unittest
from dynamicArray import DynamicArray


def test_getitem():
    dynArr = DynamicArray()


class DynamicArrayTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dynArr = DynamicArray()

    def test_len(self):
        self.assertEqual(len(self.dynArr), 0)

        self.dynArr.append(5)
        self.assertEqual(len(self.dynArr), 1)
        self.assertEqual(self.dynArr[0], 5)

        self.dynArr.append(25)
        self.assertEqual(len(self.dynArr), 2)
        self.assertEqual(self.dynArr[1], 25)

        self.dynArr.append(75)
        self.assertEqual(len(self.dynArr), 3)
        self.assertEqual(self.dynArr[2], 75)

        self.dynArr.pop()
        self.assertEqual(len(self.dynArr), 2)

    def test_append(self):
        self.assertEqual(len(self.dynArr), 0)

        self.dynArr.append(1)
        self.assertEqual(len(self.dynArr), 1)
        self.assertEqual(self.dynArr[0], 1)

        self.dynArr.append(25)
        self.assertEqual(len(self.dynArr), 2)
        self.assertEqual(self.dynArr[1], 25)


if __name__ == '__main__':
    unittest.main()
