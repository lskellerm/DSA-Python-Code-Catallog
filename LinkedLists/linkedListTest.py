import unittest
from linkedList import LinkedList


class LinkedListTest(unittest.TestCase):
    def setUp(self):
        self.empty_LinkedList = LinkedList()

        self.single_El_LinkedList = LinkedList()
        self.single_El_LinkedList.push_Front(25)

        self.multi_El_LinkedList = LinkedList()
        self.multi_El_LinkedList.push_Front(45)
        self.multi_El_LinkedList.push_Front(65)
        self.multi_El_LinkedList.push_Front(85)

    def test_init(self):
        self.assertEqual(len(self.empty_LinkedList), 0)
        self.assertIsNone(self.empty_LinkedList.head)
        self.assertEqual(self.empty_LinkedList.head, self.empty_LinkedList.tail)

    def test_len(self):
        self.assertEqual(len(self.empty_LinkedList), 0)
        self.assertEqual(len(self.single_El_LinkedList), 1)
        self.assertEqual(len(self.multi_El_LinkedList), 3)

    def test_empty(self):
        self.assertEqual(self.empty_LinkedList.is_Empty(), True)
        self.assertEqual(self.single_El_LinkedList.is_Empty(), False)
        self.assertEqual(self.multi_El_LinkedList, False)

    def test_Value_At(self):
        self.assertEqual(self.empty_LinkedList.value_At(0), None)
        self.assertEqual(self.empty_LinkedList.value_At(0), self.empty_LinkedList.head)
        self.assertEqual(self.empty_LinkedList.value_At(0), self.empty_LinkedList.tail)

        self.assertEqual(self.single_El_LinkedList.value_At(0), 25)
        self.assertEqual(self.single_El_LinkedList.value_At(0), self.single_El_LinkedList.head)
        self.assertEqual(self.single_El_LinkedList.value_At(0), self.single_El_LinkedList.tail)

        self.assertEqual(self.multi_El_LinkedList.value_At(0), 85)
        self.assertEqual(self.multi_El_LinkedList.value_At(1), 65)
        self.assertEqual(self.multi_El_LinkedList.value_At(2), 45)

    def test_Value_At_Invalid_Index(self):
        with self.assertRaises(IndexError):
            self.empty_LinkedList.value_At(1)

        with self.assertRaises(IndexError):
            self.single_El_LinkedList.value_At(1)

        with self.assertRaises(IndexError):
            self.single_El_LinkedList.value_At(-1)

        with self.assertRaises(IndexError):
            self.multi_El_LinkedList.value_At(4)

        with self.assertRaises(IndexError):
            self.multi_El_LinkedList.value_At(-1)

    def test_Push_Front_Empty_List(self):
        self.empty_LinkedList.push_Front(100)
        self.assertEqual(self.empty_LinkedList.value_At(0), 100)
        self.assertEqual(self.empty_LinkedList.head.data, 100)

        self.assertEqual(self.empty_LinkedList.head.get_next(), None)
        self.assertEqual(self.empty_LinkedList.tail, 100)
        self.assertEqual(self.empty_LinkedList.tail.get_next(), None)



if __name__ == '__main__':
        unittest.main()
