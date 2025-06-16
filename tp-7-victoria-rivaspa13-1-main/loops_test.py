import unittest.mock

import loops as ex1


class TP7LoopsTest(unittest.TestCase):

    def test_index_of(self):
        list1 = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]
        result1 = ex1.index_of("Black", list1)
        self.assertEqual(3, result1)

        result2 = ex1.index_of("Blue", list1)
        self.assertEqual(-1, result2)

        list3 = []
        result3 = ex1.index_of("Juan", list3)
        self.assertEqual(-1, result3)

    def test_index_of_by_index(self):
        list1 = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]
        result1 = ex1.index_of_by_index("Black", list1, 1)
        self.assertEqual(3, result1)

        result2 = ex1.index_of_by_index("Black", list1, 4)
        self.assertEqual(6, result2)

        result3 = ex1.index_of_by_index("Green", list1, 2)
        self.assertEqual(-1, result3)

    def test_index_of_empty(self):
        list1 = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]
        result1 = ex1.index_of_empty(list1)
        self.assertEqual(-1, result1)

        list2 = ["Red", "Green", "", "", "Pink", "", "Black"]
        result2 = ex1.index_of_empty(list2)
        self.assertEqual(2, result2)

        list3 = []
        result3 = ex1.index_of_empty(list3)
        self.assertEqual(-1, result3)

    def test_put(self):
        list1 = ["Red", "Green", "", "", "Pink", "", "Black"]
        result1 = ex1.put("Blue", list1)
        expected1_index = 2
        expected1_list = ["Red", "Green", "Blue", "", "Pink", "", "Black"]
        self.assertEqual(expected1_index, result1)
        self.assertEqual(expected1_list, list1)

        list1 = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]
        result1 = ex1.put("Blue", list1)
        expected1_index = -1
        expected1_list = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]
        self.assertEqual(expected1_index, result1)
        self.assertEqual(expected1_list, list1)

        list1 = []
        result1 = ex1.put("Blue", list1)
        expected1_index = -1
        expected1_list = []
        self.assertEqual(expected1_index, result1)
        self.assertEqual(expected1_list, list1)

    def test_remove(self):
        list1 = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]
        result1 = ex1.remove("Black", list1)
        expected1_eliminations = 2
        expected1_list = ["Red", "Green", "White", "", "Pink", "Yellow", ""]
        self.assertEqual(expected1_eliminations, result1)
        self.assertEqual(expected1_list, list1)

        list2 = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]
        result2 = ex1.remove("Blue", list1)
        expected2_eliminations = 0
        expected2_list = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]
        self.assertEqual(expected2_eliminations, result2)
        self.assertEqual(expected2_list, list2)


if __name__ == '__main__':
    unittest.main()
