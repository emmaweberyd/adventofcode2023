import unittest
from part2 import *

class TestSolution(unittest.TestCase):
        
    def test_solution(self):
        self.assertEqual(solution('test_input.txt'), 71503, "Should be 71503")


if __name__ == '__main__':
    unittest.main()