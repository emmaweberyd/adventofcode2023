import unittest
from part1 import *

class TestSolution(unittest.TestCase):

    def test_sum_of_part_numbers(self):
        self.assertEqual(sum_of_part_numbers('test_input.txt'), 4361, "Should be 4361")

if __name__ == '__main__':
    unittest.main()