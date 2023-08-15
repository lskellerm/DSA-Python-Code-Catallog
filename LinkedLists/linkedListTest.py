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

    def test_Push_Front_Nonempty_List(self):
        self.single_El_LinkedList.push_Front(100)
        self.single_El_LinkedList.push_Front(200)

        self.assertEqual(self.single_El_LinkedList.value_At(0), 200)
        self.assertEqual(self.single_El_LinkedList.head.data, 200)
        self.assertEqual(self.single_El_LinkedList.head.get_next().data, 100)

        self.assertEqual(self.single_El_LinkedList.value_At(1), 100)

        self.assertEqual(self.single_El_LinkedList.head.get_next().get_next().data, 25)
        self.assertEqual(self.single_El_LinkedList.head.get_next().get_next().get_next(), None)

        self.multi_El_LinkedList.push_Front(1)

        self.assertEqual(self.multi_El_LinkedList.value_At(0), 1)
        self.assertEqual(self.multi_El_LinkedList.head.data, 1)
        self.assertEqual(self.multi_El_LinkedList.head.get_next().data, 85)

    def test_Pop_Front_Empty_List(self):
        with self.assertRaises(Exception):
            self.empty_LinkedList.pop_Front()

    def test_Pop_Front_Single_El_List(self):
        value = self.single_El_LinkedList.pop_Front()

        self.assertEqual(value, 25)
        self.assertEqual(self.single_El_LinkedList.head, None)
        self.assertEqual(self.single_El_LinkedList.tail, None)
        self.assertEqual(self.single_El_LinkedList.head, self.single_El_LinkedList.tail)

    def test_Pop_Front_Multi_El_List(self):
        value = self.multi_El_LinkedList.pop_Front()

        self.assertEqual(value, 85)
        self.assertEqual(len(self.multi_El_LinkedList), 2)
        self.assertEqual(self.multi_El_LinkedList.head, 65)
        self.assertEqual(self.multi_El_LinkedList.head.get_next(), 45)

    def test_Push_Back_Empty_List(self):
        self.empty_LinkedList.push_Back(7)
        self.assertEqual(self.empty_LinkedList.value_At(0), 7)
        self.assertEqual(self.empty_LinkedList.tail.data, 7)
        self.assertEqual(self.empty_LinkedList.head, self.empty_LinkedList.data)

    def test_Push_Back_Non_Empty_List(self):
        old_Count = len(self.single_El_LinkedList)
        self.single_El_LinkedList.push_Back(5)

        self.assertEqual(self.single_El_LinkedList.tail.data, 5)
        self.assertEqual(self.single_El_LinkedList.tail.get_next(), None)
        self.assertEqual(len(self.single_El_LinkedList), old_Count + 1)

        old_Count = len(self.multi_El_LinkedList)
        self.multi_El_LinkedList.push_Back(5)
        self.multi_El_LinkedList.push_Back(10)
        self.multi_El_LinkedList.push_Back(15)

        self.assertEqual(self.multi_El_LinkedList.tail.data, 15)
        self.assertEqual(self.multi_El_LinkedList.tail.get_next(), None)
        self.assertEqual(len(self.multi_El_LinkedList), old_Count + 3)


if __name__ == '__main__':
        unittest.main()
