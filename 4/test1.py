import unittest
from part1 import *

class TestSolution(unittest.TestCase):

    def test_listify_numbers(self):
        self.assertEqual(listify_numbers(' 41 48 83 86 17 '), ['41', '48', '83', '86', '17'], "Should be ['41', '48', '83', '86', '17']")
        self.assertEqual(listify_numbers(' 83 86  6 31 17  9 48 53'), ['83', '86', '6', '31', '17', '9', '48', '53'], "Should be ['83', '86', '6', '31', '17', '9', '48', '53']")
        self.assertEqual(listify_numbers('     '), [], "Should be []")
        self.assertEqual(listify_numbers('   1  '), ['1'], "Should be ['1']")

    def test_wins_to_points(self):
        self.assertEqual(wins_to_points(0), 0, "Should be 0")
        self.assertEqual(wins_to_points(1), 1, "Should be 1")
        self.assertEqual(wins_to_points(2), 2, "Should be 2")
        self.assertEqual(wins_to_points(3), 4, "Should be 4")
        self.assertEqual(wins_to_points(4), 8, "Should be 8")
    
    def test_extract_numbers(self):
        self.assertEqual(extract_numbers('Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53'), (['41', '48', '83', '86', '17'], ['83', '86', '6', '31', '17', '9', '48', '53']))
        self.assertEqual(extract_numbers('Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19'), (['13', '32', '20', '16', '61'], ['61', '30', '68', '82', '17', '32', '24', '19']))
        self.assertEqual(extract_numbers('Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1'), (['1', '21', '53', '59', '44'], ['69', '82', '63', '72', '16', '21', '14', '1']))

    def test_get_number_of_wins(self):
        self.assertEqual(get_number_of_wins('Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53'), 4, "Should be 4")
        self.assertEqual(get_number_of_wins('Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19'), 2, "Should be 2")
        self.assertEqual(get_number_of_wins('Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1'), 2, "Should be 2")
        self.assertEqual(get_number_of_wins('Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83'), 1, "Should be 1")
        self.assertEqual(get_number_of_wins('Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36'), 0, "Should be 0")
        self.assertEqual(get_number_of_wins('Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'), 0, "Should be 0")

    def test_points(self):
        self.assertEqual(points('Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53'), 8, "Should be 8")
        self.assertEqual(points('Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19'), 2, "Should be 2")
        self.assertEqual(points('Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1'), 2, "Should be 2")
        self.assertEqual(points('Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83'), 1, "Should be 1")
        self.assertEqual(points('Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36'), 0, "Should be 0")
        self.assertEqual(points('Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'), 0, "Should be 0")

    def test_total_points(self):
        self.assertEqual(total_points('test_input.txt'), 13, "Should be 13")

if __name__ == '__main__':
    unittest.main()