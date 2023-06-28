import unittest
from dynamicArray import DynamicArray


class DynamicArrayTest(unittest.TestCase):
    def test_len(self):
        dynArr = DynamicArray()
        self.assertEqual(len(dynArr), 0)

        dynArr.append(5)
        self.assertEqual(len(dynArr), 1)
        self.assertEqual(dynArr[0], 5)

        dynArr.append(25)
        self.assertEqual(len(dynArr), 2)
        self.assertEqual(dynArr[1], 25)

        dynArr.append(75)
        self.assertEqual(len(dynArr), 3)
        self.assertEqual(dynArr[2], 75)

        dynArr.pop()
        self.assertEqual(len(dynArr), 2)

    def test_append(self):
        dynArr = DynamicArray()
        self.assertEqual(len(dynArr), 0)

        dynArr.append(1)
        self.assertEqual(len(dynArr), 1)
        self.assertEqual(dynArr[0], 1)

        dynArr.append(25)
        self.assertEqual(len(dynArr), 2)
        self.assertEqual(dynArr[1], 25)


if __name__ == '__main__':
    unittest.main()
