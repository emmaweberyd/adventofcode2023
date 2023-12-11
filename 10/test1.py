import unittest
from part1 import *

class TestSolution(unittest.TestCase):
    def test_path_solver(self):
        self.assertEqual(PathSolver('test_input_1.txt').nr_of_steps(), 8, "Should be 8")
        self.assertEqual(PathSolver('test_input_2.txt').nr_of_steps(), 8, "Should be 8")
        self.assertEqual(PathSolver('test_input_3.txt').nr_of_steps(), 4, "Should be 4")
        self.assertEqual(PathSolver('test_input_4.txt').nr_of_steps(), 4, "Should be 4")

if __name__ == '__main__':
    unittest.main()