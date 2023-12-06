import unittest
from part2 import *
import numpy as np
import sys

INF = 2**63 - 1

class TestSolution(unittest.TestCase):

    def test_find_lowest_location_numner(self):
        self.assertEqual(find_lowest_location_numner('test_input.txt'), 46, "Should be 46")
    
    def test_add_missing_ranges(self):
        self.assertEqual(add_missing_ranges([[[50, 98, 99], [52, 50, 97]]]), [[[0, 0, 49], [100, 100, INF], [52, 50, 97], [50, 98, 99]]])
        self.assertEqual(add_missing_ranges([[[50, 98, 99], [52, 50, 96]]]), [[[0, 0, 49], [97, 97, 97], [100, 100, INF], [52, 50, 96], [50, 98, 99]]])
        self.assertEqual(add_missing_ranges([[[50, 98, 99], [52, 50, 96]], [[50, 98, 99], [52, 50, 97]]]), [[[0, 0, 49], [97, 97, 97], [100, 100, INF], [52, 50, 96], [50, 98, 99]], [[0, 0, 49], [100, 100, INF], [52, 50, 97], [50, 98, 99]]])

    def test_intersection(self):
        self.assertEqual((intersection(np.array([79, 92]), np.array([50, 98, 99]))==np.array([])).all(), True)
        self.assertEqual((intersection(np.array([79, 92]), np.array([52, 50, 97]))==np.array([81, 94])).all(), True)
        self.assertEqual((intersection(np.array([55, 67]), np.array([50, 98, 99]))==np.array([])).all(), True)
        self.assertEqual((intersection(np.array([55, 67]), np.array([52, 50, 97]))==np.array([57, 69])).all(), True)
        self.assertEqual((intersection(np.array([0, 3]), np.array([0, 2, 48]))==np.array([0, 1])).all(), True)
        self.assertEqual((intersection(np.array([0, 3]), np.array([0, 2, INF]))==np.array([0, 1])).all(), True)
        self.assertEqual((intersection(np.array([20, 80]), np.array([0, 2, 19]))==np.array([])).all(), True)
        self.assertEqual((intersection(np.array([20, 80]), np.array([0, 2, 19]))==np.array([])).all(), True)
        self.assertEqual((intersection(np.array([8974539875347, 8974539875349]), np.array([8974539875348, 8974539875348, INF]))==np.array([8974539875348, 8974539875349])).all(), True)

        


if __name__ == '__main__':
    unittest.main()