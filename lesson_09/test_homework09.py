import unittest
from homework09 import (word_with_letter_h, string_list_sort, sum_of_pair_numbers, find_substring, sum_of_all_numbers)


class TestWordWithLetterH(unittest.TestCase):
    def test_word_with_letter_h(self):
        self.assertTrue(word_with_letter_h("Hello"))

    def test_word_without_letter_h(self):
        self.assertFalse(word_with_letter_h("World"))


class TestFindSubstring(unittest.TestCase):
    def test_str1_include_str2(self):
        self.assertTrue(find_substring("Hello, world!", "world"))

    def test_str1_not_include_str2(self):
        self.assertFalse(find_substring("The quick brown fox jumps over the lazy dog", "cat"))


class TestSumOfPairNumber(unittest.TestCase):
    def test_sum_of_pair_number_iqual(self):
        self.assertEqual(sum_of_pair_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]), 20, "Correct answer")

    def test_sum_of_pair_number_not_iqual(self):
        self.assertNotEqual(sum_of_pair_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]), 70, "Correct answer")


class TestStringListSort(unittest.TestCase):
    def test_string_list_sort_present_str(self):
        self.assertEqual(string_list_sort(['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0,
                                           'Lorem Ipsum']), ['1', '2', 'False', '6', 'Python', 'Lorem Ipsum'])

    def test_string_list_sort_not_present_str(self):
        self.assertNotEqual(string_list_sort(['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0,
                                              'Lorem Ipsum']), ['1', '2', 'False', '6', 'Lorem Ipsum'])


class TestSumOfAllNumbers(unittest.TestCase):
    def test_sum_of_all_numbers_with_numbers(self):
        self.assertEqual(sum_of_all_numbers(['1,2,3,4', '1,2,3,4,50', '1,2,3']), [10, 60, 6])

    def test_sum_of_all_numbers_with_str(self):
        self.assertIsNone(sum_of_all_numbers(['1,2,3,4', '1,2,3,4,50', 'qwerty1,2,3']))


if __name__ == '__main__':
    unittest.main()
