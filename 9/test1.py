import unittest
from part1 import *

class TestSolution(unittest.TestCase):

    def test_get_next_history_value(self):
        self.assertEqual(get_next_history_value([0, 3, 6, 9, 12, 15]), 18, "Should be 18")
        self.assertEqual(get_next_history_value([1, 3, 6, 10, 15, 21]), 28, "Should be 28")
        self.assertEqual(get_next_history_value([10, 13, 16, 21, 30, 45]), 68, "Should be 68")
        self.assertEqual(get_next_history_value([23, 45, 81, 131, 195, 273, 365, 471, 591, 725, 873, 1035, 1211, 1401, 1605, 1823, 2055, 2301, 2561, 2835, 3123]), 3425, "Should be 3425")
        self.assertEqual(get_next_history_value([0, 0, 0]), 0, "Should be 0")
        self.assertEqual(get_next_history_value([-1, -2, -3]), -4, "Should be -4")
        self.assertEqual(get_next_history_value([0]), 0, "Should be 0")


    def test_get_history_sum(self):
        self.assertEqual(get_history_sum('test_input.txt'), 114, "Should be 114")


if __name__ == '__main__':
    unittest.main()