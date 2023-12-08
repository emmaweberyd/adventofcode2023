import unittest
from part1 import *

class TestSolution(unittest.TestCase):

    def test_nr_of_steps(self):
        self.assertEqual(nr_of_steps('test_input_1.txt'), 2, "Should be 2")
        self.assertEqual(nr_of_steps('test_input_2.txt'), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()