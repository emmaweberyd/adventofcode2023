import unittest
from part2 import *

class TestSolution(unittest.TestCase):

    def test_nr_of_steps(self):
        self.assertEqual(nr_of_steps('test_input_3.txt'), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()