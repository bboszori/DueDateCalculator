import unittest
from datetime import datetime

from src.Validator import Validator


class ValidatorTestCases(unittest.TestCase):
    def setUp(self) -> None:
        self.validator = Validator()

    def test_isSubmitDateValid_true(self):
        self.assertTrue(self.validator.isSubmitDateValid(datetime(2021, 11, 2, 12, 47)))

    def test_isSubmitDateValid_false(self):
        submit_date = "2021.10.29 12:45"
        self.assertFalse(self.validator.isSubmitDateValid(submit_date))

    def test_isWorkday_true(self):
        submit_date = datetime(2021, 11, 2, 12, 47)
        self.assertTrue(self.validator.isWorkday(submit_date))

    def test_isWorkday_false(self):
        submit_date = datetime(2021, 10, 30, 12, 47)
        self.assertFalse(self.validator.isWorkday(submit_date))

    def test_isWithinWorkingHours_true(self):
        submit_date = datetime(2021, 11, 2, 12, 47)
        self.assertTrue(self.validator.isWithinWorkingHours(submit_date, 9, 17))

    def test_isWithinWorkingHours_false(self):
        submit_date = datetime(2021, 11, 2, 17, 47)
        self.assertFalse(self.validator.isWithinWorkingHours(submit_date, 9, 17))

    def test_isTurnaroundTimeValid_trueInt(self):
        ta_time = 5
        self.assertTrue(self.validator.isTurnaroundTimeValid(ta_time))

    def test_isTurnaroundTimeValid_trueFloat(self):
        ta_time = 5.2
        self.assertTrue(self.validator.isTurnaroundTimeValid(ta_time))

    def test_isTurnaroundTimeValid_false_notInt(self):
        ta_time = "5"
        self.assertFalse(self.validator.isTurnaroundTimeValid(ta_time))

    def test_isTurnaroundTimeValid_false_negative(self):
        ta_time = -1
        self.assertFalse(self.validator.isTurnaroundTimeValid(ta_time))


if __name__ == '__main__':
    unittest.main()
