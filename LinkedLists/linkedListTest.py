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
        self.assertEqual(self.empty_LinkedList.is_Empty(), True)
        self.assertIsNone(self.empty_LinkedList.head)
        self.assertEqual(self.empty_LinkedList.head, self.empty_LinkedList.tail)

    def test_len(self):
        self.assertEqual(len(self.empty_LinkedList), 0)
        self.assertEqual(len(self.single_El_LinkedList), 1)
        self.assertEqual(len(self.multi_El_LinkedList), 3)

    def test_empty(self):
        self.assertEqual(self.empty_LinkedList.is_Empty(), True)
        self.assertEqual(self.single_El_LinkedList.is_Empty(), False)
        self.assertEqual(self.multi_El_LinkedList.is_Empty(), False)

    def test_Value_At(self):
        self.assertEqual(self.single_El_LinkedList.value_At(0), 25)
        self.assertEqual(self.single_El_LinkedList.value_At(0), self.single_El_LinkedList.head)
        self.assertEqual(self.single_El_LinkedList.value_At(0), self.single_El_LinkedList.tail)

        self.assertEqual(self.multi_El_LinkedList.value_At(0), 85)
        self.assertEqual(self.multi_El_LinkedList.value_At(1), 65)
        self.assertEqual(self.multi_El_LinkedList.value_At(2), 45)

    def test_Value_At_Invalid_Index(self):
        with self.assertRaises(IndexError):
            self.empty_LinkedList.value_At(0)

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
        old_Count = len(self.single_El_LinkedList)
        self.single_El_LinkedList.push_Front(100)
        self.single_El_LinkedList.push_Front(200)

        self.assertEqual(len(self.single_El_LinkedList), old_Count + 2)
        self.assertEqual(self.single_El_LinkedList.value_At(0), 200)
        self.assertEqual(self.single_El_LinkedList.head.data, 200)
        self.assertEqual(self.single_El_LinkedList.head.get_next().data, 100)

        self.assertEqual(self.single_El_LinkedList.value_At(1), 100)

        self.assertEqual(self.single_El_LinkedList.head.get_next().get_next().data, 25)
        self.assertEqual(self.single_El_LinkedList.head.get_next().get_next().get_next(), None)

        old_Count = len(self.multi_El_LinkedList)
        self.multi_El_LinkedList.push_Front(1)

        self.assertEqual(len(self.multi_El_LinkedList), old_Count + 1)
        self.assertEqual(self.multi_El_LinkedList.value_At(0), 1)
        self.assertEqual(self.multi_El_LinkedList.head.data, 1)
        self.assertEqual(self.multi_El_LinkedList.head.get_next().data, 85)

    def test_Pop_Front_Empty_List(self):
        with self.assertRaises(Exception):
            self.empty_LinkedList.pop_Front()

    def test_Pop_Front_Single_El_List(self):
        old_Count = len(self.single_El_LinkedList)
        value = self.single_El_LinkedList.pop_Front()

        self.assertEqual(value, 25)
        self.assertEqual(self.single_El_LinkedList, old_Count - 1)
        self.assertEqual((self.single_El_LinkedList.is_Empty()), True)
        self.assertEqual(self.single_El_LinkedList.head, None)
        self.assertEqual(self.single_El_LinkedList.tail, None)

    def test_Pop_Front_Multi_El_List(self):
        old_Count = len(self.multi_El_LinkedList)
        value = self.multi_El_LinkedList.pop_Front()

        self.assertEqual(value, 85)
        self.assertEqual(self.multi_El_LinkedList, old_Count - 1)
        self.assertEqual(self.multi_El_LinkedList.head, 65)
        self.assertEqual(self.multi_El_LinkedList.head.get_next(), 45)

    def test_Push_Back_Empty_List(self):
        self.empty_LinkedList.push_Back(7)

        self.assertEqual(len(self.empty_LinkedList), 1)
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

    def test_Pop_Back_Empty_List(self):
        with self.assertRaises(Exception):
            self.empty_LinkedList.pop_Back()

    def test_Pop_Back_Single_El_List(self):
        value = self.single_El_LinkedList.pop_Back()

        self.assertEqual(value, 25)
        self.assertEqual((self.single_El_LinkedList.is_Empty()), True)

        self.assertEqual(self.single_El_LinkedList.head, None)
        self.assertEqual(self.single_El_LinkedList.tail, None)

    def test_Pop_Back_Multi_El_List(self):
        old_Count = len(self.multi_El_LinkedList)
        value = self.multi_El_LinkedList.pop_Back()

        self.assertEqual(value, 45)
        self.assertEqual(len(self.multi_El_LinkedList), old_Count - 1)
        self.assertEqual(self.multi_El_LinkedList.head, 65)
        self.assertEqual(self.multi_El_LinkedList.head.get_next(), 45)
        self.assertEqual(self.multi_El_LinkedList.head.get_next().get_next(), None)

    def test_Front_Empty_List(self):
        with self.assertRaises(Exception):
            self.empty_LinkedList.front()

    def test_Front_Non_Empty_List(self):
        value = self.single_El_LinkedList.front()
        self.assertEqual(value, 25)

        value = self.multi_El_LinkedList.front()
        self.assertEqual(value, 85)

    def test_Back_Empty_List(self):
        with self.assertRaises(Exception):
            self.empty_LinkedList.back()

    def test_Back_Non_Empty_List(self):
        value = self.single_El_LinkedList.back()
        self.assertEqual(value, 25)

        value = self.multi_El_LinkedList.back()
        self.assertEqual(value, 45)

    def test_insert_Invalid_Index(self):
        with self.assertRaises(IndexError):
            self.empty_LinkedList.insert(1, 100)

        with self.assertRaises(IndexError):
            self.single_El_LinkedList.insert(2, 25)

        with self.assertRaises(IndexError):
            self.multi_El_LinkedList.insert(-1, 40)

        with self.assertRaises(IndexError):
            self.multi_El_LinkedList.insert(5, 75)

    def test_Insert_Empty_List(self):
        self.empty_LinkedList.insert(0, 50)
        self.assertEqual(self.empty_LinkedList.value_At(0), 50)
        self.assertEqual(self.empty_LinkedList.head.get_next().data, None)

    def test_Insert_Non_Empty_List(self):
        self.single_El_LinkedList.insert(0, 45)
        self.assertEqual(self.single_El_LinkedList.value_At(0), 45)
        self.assertEqual(len(self.single_El_LinkedList), 2)
        self.assertEqual(self.single_El_LinkedList.head.get_next().data, 25)

        old_Count = len(self.multi_El_LinkedList)
        old_Value = self.multi_El_LinkedList.value_At(1)
        self.multi_El_LinkedList.insert(1, 75)
        self.assertEqual(self.multi_El_LinkedList.value_At(1), 75)
        self.assertEqual(len(self.multi_El_LinkedList), old_Count + 1)
        self.assertEqual(self.multi_El_LinkedList.head.get_next().get_next().data, old_Value)

    def test_Insert_At_End(self):
        old_Tail_Value = self.single_El_LinkedList.tail
        self.single_El_LinkedList.insert(len(self.single_El_LinkedList) - 1, 200)
        self.assertEqual(self.single_El_LinkedList.tail.data, 100)
        self.assertEqual(self.single_El_LinkedList.tail.get_next, None)
        self.assertEqual(len(self.single_El_LinkedList), 2)
        self.assertEqual(self.single_El_LinkedList.value_At(len(self.single_El_LinkedList) - 2), old_Tail_Value)

        old_Tail_Value = self.multi_El_LinkedList.tail
        self.multi_El_LinkedList.insert(len(self.multi_El_LinkedList) - 1, 2)
        self.assertEqual(self.multi_El_LinkedList.tail.data, 2)
        self.assertEqual(self.multi_El_LinkedList.tail.get_next, None)
        self.assertEqual(len(self.multi_El_LinkedList), 2)
        self.assertEqual(self.multi_El_LinkedList.value_At(len(self.multi_El_LinkedList) - 2), old_Tail_Value)

    def test_Erase_Invalid_Index(self):
        with self.assertRaises(IndexError):
            self.single_El_LinkedList.erase(1)

        with self.assertRaises(IndexError):
            self.multi_El_LinkedList.erase(-1)

        with self.assertRaises(IndexError):
            self.multi_El_LinkedList.erase(len(self.multi_El_LinkedList))

    def test_Erase_Empty_List(self):
        with self.assertRaises(Exception):
            self.empty_LinkedList.erase(0)

    def test_Erase_Single_El_List(self):
        self.single_El_LinkedList.erase(0)

        self.assertEqual(self.single_El_LinkedList.is_Empty(), True)
        self.assertEqual(self.single_El_LinkedList.head, None)
        self.assertEqual(self.single_El_LinkedList.head, self.single_El_LinkedList.tail)
        self.assertEqual(len(self.single_El_LinkedList), 0)

    def test_Erase_Multi_El_List(self):
        old_Count = len(self.multi_El_LinkedList)
        self.multi_El_LinkedList.erase(1)

        self.assertEqual(len(self.multi_El_LinkedList), old_Count - 1)
        self.assertNotEqual(self.multi_El_LinkedList.value_At(1), 65)
        self.assertEqual(self.multi_El_LinkedList.head.get_next().data, 45)

    def test_Erase_At_End(self):
        old_Count = len(self.multi_El_LinkedList)
        self.multi_El_LinkedList.erase(old_Count - 1)  # Erases the node at the end of the linked list

        self.assertEqual(len(self.multi_El_LinkedList), old_Count - 1)
        self.assertNotEqual(self.multi_El_LinkedList.tail.data, 45)
        self.assertEqual(self.multi_El_LinkedList.tail.data, 65)
        self.assertEqual(self.multi_El_LinkedList.tail, None)

    def test_Value_From_End_Invalid_Index(self):
        with self.assertRaises(IndexError):
            self.empty_LinkedList.value_From_End(1)

        with self.assertRaises(IndexError):
            self.single_El_LinkedList(len(self.single_El_LinkedList))

        with self.assertRaises(IndexError):
            self.single_El_LinkedList.value_From_End(-1)

        with self.assertRaises(IndexError):
            self.multi_El_LinkedList.value_From_End((len(self.multi_El_LinkedList)))

        with self.assertRaises(IndexError):
            self.multi_El_LinkedList.value_From_End(-1)

    def test_Value_From_End_Non_Empty_List(self):
        value = self.single_El_LinkedList.value_From_End(0)
        self.assertEqual(value, 25)

        value = self.multi_El_LinkedList.value_From_End(0)
        self.assertEqual(value, 45)

        value = self.multi_El_LinkedList.value_From_End(1)
        self.assertEqual(value, 65)

    def test_Reverse(self):
        self.empty_LinkedList.reverse()
        self.assertTrue(self.empty_LinkedList.is_Empty())

        self.single_El_LinkedList.reverse()
        self.assertEqual(self.single_El_LinkedList.value_At(0), 25)
        self.assertEqual(self.single_El_LinkedList.head, self.single_El_LinkedList.tail)

        reversed_List = [45, 65, 85]
        self.multi_El_LinkedList.reverse()

        current = self.multi_El_LinkedList.head

        for value in reversed_List:
            self.assertEqual(current.data, value)
            current = current.get_Next()

    def test_Remove_Value_Empty(self):
        with self.assertRaises(Exception):
            self.empty_LinkedList.remove_Value(5)

    def test_Remove_Value_Not_Found(self):
        with self.assertRaises(ValueError):
            self.single_El_LinkedList.remove_Value(10)

        with self.assertRaises(ValueError):
            self.multi_El_LinkedList.remove_Value(25)

    def test_Remove_Value_Single_El_List(self):
        self.single_El_LinkedList.remove_Value(25)

        self.assertEqual(len(self.single_El_LinkedList), 0)
        self.assertTrue(self.single_El_LinkedList.is_Empty())
        self.assertIsNone(self.single_El_LinkedList.head)
        self.assertIsNone(self.single_El_LinkedList.tail)

    def test_Remove_Value_Multi_El_List(self):
        old_Count = len(self.multi_El_LinkedList)
        old_Value = self.multi_El_LinkedList.value_At(2)

        self.multi_El_LinkedList.remove_Value(65)

        self.assertEqual(len(self.multi_El_LinkedList), old_Count - 1)
        self.assertNotEqual(self.multi_El_LinkedList.head.get_next().data, old_Value)

    def test_Remove_Value_Multi_El_List_Head(self):
        old_Count = len(self.multi_El_LinkedList)
        old_Head = self.multi_El_LinkedList.head.data

        self.multi_El_LinkedList.remove_value(85)

        self.assertEqual(len(self.multi_El_LinkedList), old_Count - 1)
        self.assertNotEqual(self.multi_El_LinkedList.head.data, old_Head)

    def test_Remove_Value_Multi_El_List_Tail(self):
        old_Count = len(self.multi_El_LinkedList)
        old_Tail = self.multi_El_LinkedList.tail.data

        self.multi_El_LinkedList.remove_Value(45)

        self.assertEqual(len(self.multi_El_LinkedList), old_Count - 1)
        self.assertNotEqual(self.multi_El_LinkedList.tail.data, old_Tail)
        self.assertIsNone(self.multi_El_LinkedList.tail.get_next())

if __name__ == '__main__':
    unittest.main()
