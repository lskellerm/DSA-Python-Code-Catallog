import unittest
from dynamicArray import DynamicArray


class DynamicArrayTest(unittest.TestCase):
    def setUp(self):
        self.dynArr = DynamicArray()

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

    def test_getitem(self):
        print(self.dynArr)
        self.dynArr.append(15)
        self.dynArr.append(5)
        self.dynArr.append(2)
        self.dynArr.append(9)

        self.assertEqual((self.dynArr[0]), 15)
        self.assertEqual((self.dynArr[1]), 5)
        self.assertEqual((self.dynArr[2]), 2)
        self.assertEqual((self.dynArr[3]), 9)

    def test_setitem(self):
        self.dynArr.append(None)
        self.dynArr.append(None)

        self.dynArr[0] = 7
        self.dynArr[1] = 30

        self.assertEqual(self.dynArr[0], 7)
        self.assertEqual(self.dynArr[1], 30)

    def test_str(self):
        self.dynArr.append(5)
        self.dynArr.append(10)
        self.dynArr.append(15)

        expected_array = '[5, 10, 15]'

        self.assertEqual((str(self.dynArr)), expected_array)

    def test_is_empty(self):
        self.assertEqual(self.dynArr.is_empty(), True)
        self.dynArr.append(5)
        self.assertEqual(self.dynArr.is_empty(), False)

    def test_append(self):
        self.assertEqual(len(self.dynArr), 0)

        self.dynArr.append(1)
        self.assertEqual(len(self.dynArr), 1)
        self.assertEqual(self.dynArr[0], 1)

        self.dynArr.append(25)
        self.assertEqual(len(self.dynArr), 2)
        self.assertEqual(self.dynArr[1], 25)

    def test_pop(self):
        self.dynArr.append(8)
        self.dynArr.append(1)
        self.dynArr.append(5)
        self.dynArr.append(3)

        self.assertEqual((self.dynArr.pop()), 3)
        self.assertEqual(len(self.dynArr), 3)

        self.assertEqual((self.dynArr.pop(0)), 8)
        self.assertEqual(len(self.dynArr), 2)

    def test_remove(self):
        self.dynArr.append(1)
        self.dynArr.append(10)
        self.dynArr.append(6)

        self.dynArr.remove(10)

        self.assertEqual(len(self.dynArr), 2)
        self.assertNotEqual(self.dynArr[1], 10)
        self.assertEqual(self.dynArr[1], 6)

    def test_removeAll(self):
        self.dynArr.append(1)
        self.dynArr.append(10)
        self.dynArr.append(6)
        self.dynArr.append(10)
        self.dynArr.append(5)
        self.dynArr.append(10)
        self.dynArr.append(8)

        expected_Array = [i for i in self.dynArr if i != 10]
        self.dynArr.removeAll(10)

        self.assertEqual(len(self.dynArr), len(expected_Array))

        for i in range(len(expected_Array)):
            self.assertEqual(self.dynArr[i], expected_Array[i])

    def test_insert(self):
        self.dynArr.append(1)
        self.dynArr.append(10)
        self.dynArr.append(8)

        self.dynArr.insert(2, 15)

        self.assertEqual(self.dynArr[2], 15)



if __name__ == '__main__':
    unittest.main()
