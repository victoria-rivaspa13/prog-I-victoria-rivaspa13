import unittest.mock

import loops_and_print as ex1


class TP7LoopsAndPrintTest(unittest.TestCase):

    def test_enumerate_list(self):
        list1 = ["Red", "Green", "", "", "White", "", "Black"]
        result1 = ex1.enumerate_list(list1)
        expected1 = ["0. Red", "1. Green", "2. White", "3. Black"]
        self.assertEqual(expected1, result1)

        list2 = ['Audi']
        result2 = ex1.enumerate_list(list2)
        expected2 = ["0. Audi"]
        self.assertEqual(expected2, result2)

        list3 = []
        result3 = ex1.enumerate_list(list3)
        expected3 = []
        self.assertEqual(expected3, result3)

    def test_enumerate_backwards(self):
        list1 = ["Red", "Green", "", "White", "Black"]
        result1 = ex1.enumerate_backwards(list1)
        expected1 = ["0. deR", "1. neerG", "2. etihW", "3. kcalB"]
        self.assertEqual(expected1, result1)

        list2 = []
        result2 = ex1.enumerate_backwards(list2)
        expected2 = []
        self.assertEqual(expected2, result2)

        list3 = ['Audi', ""]
        result3 = ex1.enumerate_backwards(list3)
        expected3 = ["0. iduA"]
        self.assertEqual(expected3, result3)


if __name__ == '__main__':
    unittest.main()
