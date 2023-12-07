import unittest
from part1 import *

class TestSolution(unittest.TestCase):

    def test_hand_type(self):
        self.assertEqual(hand_type(['32T3K', '765']), 1, "Should be 1")
        self.assertEqual(hand_type(['T55J5', '684']), 3, "Should be 3")
        self.assertEqual(hand_type(['KK677', '28']), 2, "Should be 2")
        self.assertEqual(hand_type(['KTJJT', '220']), 2, "Should be 2")
        self.assertEqual(hand_type(['QQQJA', '483']), 3, "Should be 3")
        self.assertEqual(hand_type(['QQQQQ', '483']), 6, "Should be 6")
        self.assertEqual(hand_type(['QQQQ1', '483']), 5, "Should be 5")
        self.assertEqual(hand_type(['Q1QQ1', '483']), 4, "Should be 4")
        self.assertEqual(hand_type(['12345', '483']), 0, "Should be 0")

    def test_solution(self):
        self.assertEqual(solution('test_input.txt'), 6440, "Should be 6440")

    def test_sort_hands(self):
        self.assertEqual(sort_hands([['32T3K', '765'], ['T55J5', '684'], ['KK677', '28'], ['KTJJT', '220'], ['QQQJA', '483']]), [['32T3K', '765'], ['KTJJT', '220'], ['KK677', '28'], ['T55J5', '684'], ['QQQJA', '483']])

if __name__ == '__main__':
    unittest.main()