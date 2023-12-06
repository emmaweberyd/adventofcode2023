import unittest
from part1 import *

class TestSolution(unittest.TestCase):

    def test_get_distance(self):
        self.assertEqual(get_distance(7, 0), 0)
        self.assertEqual(get_distance(7, 1), 6)
        self.assertEqual(get_distance(7, 2), 10)
        self.assertEqual(get_distance(7, 3), 12)
        self.assertEqual(get_distance(7, 4), 12)
        self.assertEqual(get_distance(7, 5), 10)
        self.assertEqual(get_distance(7, 6), 6)
        self.assertEqual(get_distance(7, 7), 0)

    def test_nr_of_ways_to_win(self):
        self.assertEqual(nr_of_ways_to_win([7, 9]), 4)
        self.assertEqual(nr_of_ways_to_win([15, 40]), 8)
        self.assertEqual(nr_of_ways_to_win([30, 200]), 9)
        
    def test_solution(self):
        self.assertEqual(solution('test_input.txt'), 288, "Should be 288")


if __name__ == '__main__':
    unittest.main()