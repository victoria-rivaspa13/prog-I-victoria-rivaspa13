import unittest.mock

import maps_loops as ex1

class TP10MapsTest(unittest.TestCase):

    def test_find_max(self):
        result1 = ex1.find_max_value({'John': 85, 'Emma': 92, 'Sophia': 78})
        self.assertEqual(result1, "Emma")

        result = ex1.find_max_value({})
        self.assertEqual(result, "")


    def test_reverse_dict(self):
        result1 = ex1.reverse_dict({'a': 1, 'b': 2, 'c': 3, 'd': 3, 'e': 2})
        self.assertEqual({1: 'a', 2: 'be', 3: 'cd'}, result1)

        result2 = ex1.reverse_dict({})
        self.assertEqual({}, result2)


    def test_word_frequency(self):
        result1 = ex1.word_freq_counter(["apple", "banana", "apple", "orange", "banana", "apple"])
        self.assertEqual({'apple': 3, 'banana': 2, 'orange': 1}, result1)

        result2 = ex1.word_freq_counter("")
        self.assertEqual({}, result2)

    def test_biggest_expense(self):
        result1 = ex1.find_biggest_expense({'Food': [60, 80, 100], 'Transport': [10, 1, 2], 'Games': [10, 20, 30]})
        self.assertEqual("Food", result1)

        result2 = ex1.find_biggest_expense({})
        self.assertEqual("", result2)

    def test_sum_of_expenses(self):
        result1 = ex1.sum_of_expenses({'Food': [60, 80, 100], 'Transport': [10, 1, 2], 'Games': [10, 20, 30]})
        self.assertEqual({'Food': 240, 'Transport': 13, 'Games': 60}, result1)

        result2 = ex1.sum_of_expenses({})
        self.assertEqual({}, result2)

    def test_sum_of_expenses_by_type(self):
        result1 = ex1.sum_of_expenses_by_type({'Food': [("A", 60), ("B", 100), ("A", 20)], 'Transport': [("A", 10), ("B", 50), ("C", 5)], 'Games': [("A", 6), ("B", 24), ("C", 99)]})
        self.assertEqual({'A': 96, 'B': 174, 'C': 104}, result1)

        result2 = ex1.sum_of_expenses_by_type({})
        self.assertEqual({}, result2)


if __name__ == '__main__':
    unittest.main()
