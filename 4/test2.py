import unittest
from part2 import *

class TestSolution(unittest.TestCase):

    def test_final_scratchcard_count(self):
        self.assertEqual(final_scratchcard_count('test_input.txt'), 30, "Should be 30")
        self.assertEqual(final_scratchcard_count('test_input_1.txt'), 1, "Should be 1")
        self.assertEqual(final_scratchcard_count('test_input_2.txt'), 1, "Should be 1")

if __name__ == '__main__':
    unittest.main()