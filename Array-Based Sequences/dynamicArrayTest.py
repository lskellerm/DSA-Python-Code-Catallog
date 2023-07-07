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
        self.assertTrue(self.dynArr.is_empty())
        self.dynArr.append(5)
        self.assertFalse(self.dynArr.is_empty())

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

    def test_clear(self):
        self.dynArr.append(1)
        self.dynArr.append(10)
        self.dynArr.append(8)

        self.dynArr.clear()

        self.assertEqual(len(self.dynArr), 0)
        self.assertEqual(str(self.dynArr), str([]))
        self.assertTrue(self.dynArr.is_empty())

    def test_index(self):
        self.dynArr.append(1)
        self.dynArr.append(10)
        self.dynArr.append(8)

        self.assertEqual(self.dynArr.index(8), 2)
        self.assertEqual(self.dynArr.index(15), -1)

    def test_count(self):
        self.dynArr.append(1)
        self.dynArr.append(10)
        self.dynArr.append(8)
        self.dynArr.append(10)
        self.dynArr.append(10)
        self.dynArr.append(8)

        self.assertEqual(self.dynArr.count(10), 3)
        self.assertEqual(self.dynArr.count(5), 0)

    def test_reverse(self):
        self.dynArr.append(1)
        self.dynArr.append(10)
        self.dynArr.append(8)
        self.dynArr.append(5)
        self.dynArr.append(9)

        reversed_list = [9, 5, 8, 10, 1]
        self.dynArr.reverse()
        self.assertEqual(len(self.dynArr), len(reversed_list))

        for i in range(len(reversed_list)):
            self.assertEqual(self.dynArr[i], reversed_list[i])

    def test_extend(self):
        self.dynArr.append(1)
        self.dynArr.append(10)
        self.dynArr.append(8)

        dynArr2 = DynamicArray()
        dynArr2.append(2)
        dynArr2.append(1)
        dynArr2.append(4)

        extended_Array_Length = len(self.dynArr) + len(dynArr2)
        self.dynArr.extend(dynArr2)

        self.assertEqual(len(self.dynArr), extended_Array_Length)

        self.assertEqual(self.dynArr[3], dynArr2[0])
        self.assertEqual(self.dynArr[4], dynArr2[1])
        self.assertEqual(self.dynArr[5], dynArr2[2])

    def test_copy(self):
        self.dynArr.append(1)
        self.dynArr.append(10)
        self.dynArr.append(8)

        dynArrayCopy = self.dynArr.copy()

        self.assertIsNot(self.dynArr, dynArrayCopy)
        self.assertEqual(len(dynArrayCopy), len(self.dynArr))
        self.assertEqual(str(self.dynArr), str(dynArrayCopy))

    def test_sort(self):
        self.dynArr.append(21)
        self.dynArr.append(14)
        self.dynArr.append(1)
        self.dynArr.append(13)
        self.dynArr.append(100)

        expected_Sorted_Array_Asc = '[1, 13, 14, 21, 100]'

        self.dynArr.sort('ascending')
        self.assertEqual(len(self.dynArr), 5)
        self.assertEqual(str(self.dynArr), expected_Sorted_Array_Asc)

        expected_Sorted_Array_Desc = '[100, 21, 14, 13, 1]'

        self.dynArr.sort('descending')
        self.assertEqual(len(self.dynArr), 5)
        self.assertEqual(str(self.dynArr), expected_Sorted_Array_Desc)

    def test_setitem_invalid_index(self):
        self.dynArr.append(10)

        with self.assertRaises(IndexError):
            self.dynArr[1] = 20

    def test_getitem_invalid_index(self):
        self.dynArr.append(10)

        with self.assertRaises(IndexError):
            item = self.dynArr[1]

if __name__ == '__main__':
    unittest.main()
