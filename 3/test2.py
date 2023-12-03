import unittest
from part2 import *

class TestSolution(unittest.TestCase):

    def test_get_ratio_sum(self):
        self.assertEqual(get_ratio_sum('test_input.txt'), 467835, "Should be 467835")

if __name__ == '__main__':
    unittest.main()