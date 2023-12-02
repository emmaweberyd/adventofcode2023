import unittest
from part1 import *

class TestSolution(unittest.TestCase):

    def test_max_cube_count(self):
        self.assertEqual(max_cube_count('Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green', 'blue'), 6, "Should be 6")
        self.assertEqual(max_cube_count('Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green', 'green'), 2, "Should be 2")
        self.assertEqual(max_cube_count('Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green', 'red'), 4, "Should be 4")

    def test_is_possible(self):
        self.assertEqual(is_possible('Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'), True, "Should be True")
        self.assertEqual(is_possible('Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue'), True, "Should be True")
        self.assertEqual(is_possible('Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red'), False, "Should be False")
        self.assertEqual(is_possible('Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red'), False, "Should be False")
        self.assertEqual(is_possible('Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'), True, "Should be True")

    def test_get_id_sum_of_possible_games(self):
        self.assertEqual(get_id_sum_of_possible_games('test_input.txt'), 8, "Should be 8")

if __name__ == '__main__':
    unittest.main()