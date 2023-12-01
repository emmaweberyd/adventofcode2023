import unittest
from functions1 import *

class TestSolution(unittest.TestCase):

    def test_get_first_digit(self):
        self.assertEqual(get_first_digit('1'), '1', "Should be 1")
        self.assertEqual(get_first_digit('b1'), '1', "Should be 1")
        self.assertEqual(get_first_digit('b21'), '2', "Should be 2")
        self.assertEqual(get_first_digit('dfsdfsdfehrtjbfhrth0ffdsfew'), '0', "Should be 0")

    def test_get_last_digit(self):
        self.assertEqual(get_last_digit('1'), '1', "Should be 1")
        self.assertEqual(get_last_digit('b1'), '1', "Should be 1")
        self.assertEqual(get_last_digit('b21'), '1', "Should be 1")
        self.assertEqual(get_last_digit('dfsdfsdfehrtjbfhrth0ffdsfew7fewfew'), '7', "Should be 7")

    def test_get_calibration_value(self):
        self.assertEqual(get_calibration_value('1abc2'), 12, "Should be 12")
        self.assertEqual(get_calibration_value('pqr3stu8vwx'), 38, "Should be 38")
        self.assertEqual(get_calibration_value('a1b2c3d4e5f'), 15, "Should be 15")
        self.assertEqual(get_calibration_value('treb7uchet'), 77, "Should be 77")

if __name__ == '__main__':
    unittest.main()