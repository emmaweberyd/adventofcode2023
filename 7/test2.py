import unittest
from part2 import *

class TestSolution(unittest.TestCase):

    def test_hand_type(self):
        self.assertEqual(hand_type(['32T3K', '765']), 1, "Should be 1")
        self.assertEqual(hand_type(['KK677', '28']), 2, "Should be 2")
        self.assertEqual(hand_type(['T55J5', '684']), 5, "Should be 5")
        self.assertEqual(hand_type(['KTJJT', '220']), 5, "Should be 5")
        self.assertEqual(hand_type(['QQQJA', '483']), 5, "Should be 5")
        self.assertEqual(hand_type(['QQJQQ', '483']), 6, "Should be 6")
        self.assertEqual(hand_type(['QQQQ1', '483']), 5, "Should be 5")
        self.assertEqual(hand_type(['Q1QQ1', '483']), 4, "Should be 4")
        self.assertEqual(hand_type(['12345', '483']), 0, "Should be 0")
        self.assertEqual(hand_type(['1234J', '483']), 1, "Should be 1")
        self.assertEqual(hand_type(['JJJJJ', '483']), 6, "Should be 6")

    def test_solution(self):
        self.assertEqual(solution('test_input.txt'), 5905, "Should be 5905")

    def test_sort_hands(self):
        self.assertEqual(sort_hands([['32T3K', '765'], ['T55J5', '684'], ['KK677', '28'], ['KTJJT', '220'], ['QQQJA', '483']]), [['32T3K', '765'], ['KK677', '28'], ['T55J5', '684'], ['QQQJA', '483'], ['KTJJT', '220']])

if __name__ == '__main__':
    unittest.main()