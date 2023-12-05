import unittest
from part1 import *

class TestSolution(unittest.TestCase):

    def test_convert(self):
        self.assertEqual(convert(79, [['50', '98', '2'], ['52', '50', '48']]), 81, "Should be 81")
        self.assertEqual(convert(14, [['50', '98', '2'], ['52', '50', '48']]), 14, "Should be 14")
        self.assertEqual(convert(55, [['50', '98', '2'], ['52', '50', '48']]), 57, "Should be 57")
        self.assertEqual(convert(13, [['50', '98', '2'], ['52', '50', '48']]), 13, "Should be 13") 
        self.assertEqual(convert(14, [['0', '15', '37'], ['37', '52', '2'], ['39', '0', '15']]), 53, "Should be 53")
        self.assertEqual(convert(1, [['2067746708', '1', '124423068']]), 2067746708, "Should be 2067746708")

    def test_find_lowest_location_numner(self):
        self.assertEqual(find_lowest_location_numner('test_input.txt'), 35, "Should be 35")


if __name__ == '__main__':
    unittest.main()