import unittest
from part2 import *

class TestSolution(unittest.TestCase):

    def test_find_lowest_location_numner(self):
        self.assertEqual(find_lowest_location_numner('test_input.txt'), 46, "Should be 46")


if __name__ == '__main__':
    unittest.main()