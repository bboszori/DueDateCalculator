import unittest
from src.DueDateCalculator import DueDateCalculator
from datetime import datetime


class DueDateCalculatorTestCases(unittest.TestCase):
    def setUp(self) -> None:
        self.dueDateCalc = DueDateCalculator()
        self.startHour = self.dueDateCalc.startHour
        self.endHour = self.dueDateCalc.endHour
        self.submit_date = datetime(2021, 11, 2, 10, 45)
        self.ta_time = 5

    def test_validateInput_submitDatetype(self):
        submit_date = "2021.10.27 10:22"
        with self.assertRaises(TypeError) as cm:
            self.dueDateCalc.validateInput(submit_date, self.ta_time)
        self.assertEqual("Submit date must be given in datetime type", str(cm.exception))

    def test_validateInput_TurnaroundTimetype(self):
        ta_time = "2"
        with self.assertRaises(TypeError) as cm:
            self.dueDateCalc.validateInput(self.submit_date, ta_time)
        self.assertEqual("Turnaround time must be a positive number", str(cm.exception))

    def test_validateInput_ServiceTime(self):
        submit_date = datetime(2021, 11, 2, 19, 45)
        with self.assertRaises(ValueError) as cm:
            self.dueDateCalc.validateInput(submit_date, self.ta_time)
        self.assertTrue(
            "Submit date must be in service time: on workdays between " + str(self.startHour) + " and " + str(
                self.endHour) + " hours" in str(cm.exception))

    def test_nextIsWorkday_true(self):
        self.assertTrue(self.dueDateCalc.nextIsWorkday(self.submit_date))

    def test_nextIsWorkday_false(self):
        self.assertFalse(self.dueDateCalc.nextIsWorkday(datetime(2021, 11, 5, 12, 12)))

    def test_remainingMinfromDay_min(self):
        submit_date = datetime(2021, 11, 2, 16, 45)
        self.assertEqual(self.dueDateCalc.remainingMinfromDay(submit_date), 15)

    def test_remainingMinfromDay_hours(self):
        submit_date = datetime(2021, 11, 2, 10, 0)
        self.assertEqual(self.dueDateCalc.remainingMinfromDay(submit_date), 420)

    def test_calcDueDate_days(self):
        ta_time = 16
        self.assertEqual(self.dueDateCalc.CalculateDueDate(self.submit_date, ta_time), datetime(2021, 11, 4, 10, 45))

    def test_calcDueDate_friday(self):
        ta_time = 24
        submit_date = datetime(2021, 11, 5, 10, 45)
        self.assertEqual(self.dueDateCalc.CalculateDueDate(submit_date, ta_time), datetime(2021, 11, 10, 10, 45))

    def test_calcDueDate_withinaday(self):
        ta_time = 4
        self.assertEqual(self.dueDateCalc.CalculateDueDate(self.submit_date, ta_time), datetime(2021, 11, 2, 14, 45))

    def test_calcDueDate_overaday(self):
        ta_time = 7
        self.assertEqual(self.dueDateCalc.CalculateDueDate(self.submit_date, ta_time), datetime(2021, 11, 3, 9, 45))

    def test_calcDueDate_halfhour(self):
        ta_time = 0.5
        submit_date = datetime(2021, 11, 5, 16, 45)
        self.assertEqual(self.dueDateCalc.CalculateDueDate(submit_date, ta_time), datetime(2021, 11, 8, 9, 15))

    def test_calcDueDate_week(self):
        ta_time = 41
        self.assertEqual(self.dueDateCalc.CalculateDueDate(self.submit_date, ta_time), datetime(2021, 11, 9, 11, 45))


if __name__ == '__main__':
    unittest.main()
