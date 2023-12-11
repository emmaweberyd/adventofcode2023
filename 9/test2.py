import unittest
from part2 import *

class TestSolution(unittest.TestCase):

    def test_get_prev_history_value(self):
        self.assertEqual(get_prev_history_value([0, 3, 6, 9, 12, 15]), -3, "Should be -3")
        self.assertEqual(get_prev_history_value([1, 3, 6, 10, 15, 21]), 0, "Should be 0")
        self.assertEqual(get_prev_history_value([10, 13, 16, 21, 30, 45]), 5, "Should be 5")

    def test_get_history_sum(self):
        self.assertEqual(get_history_sum('test_input.txt'), 2, "Should be 2")


if __name__ == '__main__':
    unittest.main()