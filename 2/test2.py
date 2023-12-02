import unittest
from part2 import *

class TestSolution(unittest.TestCase):

    def test_get_minimum_set_of_cubes(self):
        self.assertEqual(get_minimum_set_of_cubes('Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'), (4, 2, 6), "Should be (4, 2, 6)")
        self.assertEqual(get_minimum_set_of_cubes('Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue'),  (1, 3, 4), "Should be (1, 3, 4)")
        self.assertEqual(get_minimum_set_of_cubes('Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red'), (20, 13, 6), "Should be (20, 13, 6)")
        self.assertEqual(get_minimum_set_of_cubes('Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red'), (14, 3, 15), "Should be (14, 3, 15)")
        self.assertEqual(get_minimum_set_of_cubes('Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'), (6, 3, 2), "Should be (6, 3, 2)")

    def test_get_minimum_cube_set_power(self):
        self.assertEqual(get_minimum_cube_set_power('Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'), 48, "Should be 48")
        self.assertEqual(get_minimum_cube_set_power('Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue'),  12, "Should be 12")
        self.assertEqual(get_minimum_cube_set_power('Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red'), 1560, "Should be 1560")
        self.assertEqual(get_minimum_cube_set_power('Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red'), 630, "Should be 630")
        self.assertEqual(get_minimum_cube_set_power('Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'), 36, "Should be 36")

    def test_sum_of_minimum_cub_set_powers(self):
        self.assertEqual(sum_of_minimum_cub_set_powers('test_input.txt'), 2286, "Should be 2286")

if __name__ == '__main__':
    unittest.main()