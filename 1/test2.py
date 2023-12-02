import unittest
from functions2 import *

class TestSolution(unittest.TestCase):

    def test_find_first_digit(self):
        self.assertEqual(find_first_digit('two1nine'), '2', "Should be 2")
        self.assertEqual(find_first_digit('eightwothree'), '8', "Should be 8")
        self.assertEqual(find_first_digit('eight'), '8', "Should be 8")
    
    def test_find_last_digit(self):
        self.assertEqual(find_last_digit('two1nine'), '9', "Should be 9")
        self.assertEqual(find_last_digit('eightwothree'), '3', "Should be 3")
        self.assertEqual(find_last_digit('eight'), '8', "Should be 8")

    def test_get_calibration_value(self):
        self.assertEqual(get_calibration_value('two1nine'), 29, "Should be 29")
        self.assertEqual(get_calibration_value('eightwothree'), 83, "Should be 83")
        self.assertEqual(get_calibration_value('abcone2threexyz'), 13, "Should be 13")
        self.assertEqual(get_calibration_value('xtwone3four'), 24, "Should be 24")
        self.assertEqual(get_calibration_value('4nineeightseven2'), 42, "Should be 4")
        self.assertEqual(get_calibration_value('zoneight234'), 14, "Should be 14")
        self.assertEqual(get_calibration_value('7pqrstsixteen'), 76, "Should be 76")
        self.assertEqual(get_calibration_value('6'), 66, "Should be 66")
        self.assertEqual(get_calibration_value('6twofive3two'), 62, "Should be 62")
        self.assertEqual(get_calibration_value('2312'), 22, "Should be 22")
        

    def test_get_calibration_sum(self):
        self.assertEqual(get_calibration_sum('test_input.txt'), 281, "Should be 281")

if __name__ == '__main__':
    unittest.main()