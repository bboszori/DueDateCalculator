from src.DueDateCalculator_abstract import DueDateCalcAbstract
from src.Validator import Validator
from datetime import datetime, timedelta


class DueDateCalculator(DueDateCalcAbstract):
    """ Class for calculating due dates

        Attributes
        ----------
        startHour : int
            start of working hours, default value is 9
        endHour : int
            end of working hours, default value is 17
     """

    def __init__(self, start_hour=9, end_hour=17):
        self.validator = Validator()
        self.startHour = start_hour
        self.endHour = end_hour

    def validateInput(self, submit_date, turnaround_time):
        """ Validates submit_date and turnaround_time for the calculator"""

        if not Validator.isSubmitDateValid(submit_date):
            raise TypeError("Submit date must be given in datetime type")

        if not Validator.isTurnaroundTimeValid(turnaround_time):
            raise TypeError("Turnaround time must be a positive number")

        if not self.validator.isInServiceTime(submit_date, self.startHour, self.endHour):
            raise ValueError(
                "Submit date must be in service time: on workdays between " + str(self.startHour) + " and " + str(
                    self.endHour) + " hours")

    def nextIsWorkday(self, due_date):
        """ Returns True if next day to due_date is workday """
        return Validator.isWorkday(due_date + timedelta(days=1))

    def remainingMinfromDay(self, submit_date):
        """ Returns the remaining minutes till the end of work day """
        end_of_day = datetime(submit_date.year, submit_date.month, submit_date.day, self.endHour, 0)
        return (end_of_day - submit_date).seconds // 60

    def CalculateDueDate(self, submit_date, turnaround_time):
        """ Returns the calculated due date based on the submit_day and the given turnaround time """
        self.validateInput(submit_date, turnaround_time)

        remaining_days = turnaround_time // 8  # whole days from turnaround time
        remaining_minutes = int((turnaround_time % 8) * 60)  # remaining part of turnaround time in minutes
        remaining_from_start_day = self.remainingMinfromDay(submit_date)
        due_date = submit_date

        # if turnaround time is more than a day, then adding the whole days to submit date
        while remaining_days > 0:
            if self.nextIsWorkday(due_date):
                due_date += timedelta(days=1)
                remaining_days -= 1
            else:
                due_date += timedelta(days=1)

        # if remaining part of the turnaround time can be finished on the current workday,
        # then adding the minutes to the due_date
        if remaining_from_start_day >= remaining_minutes:
            due_date += timedelta(minutes=remaining_minutes)
        # if remaining part of the turnaround time can't be finished on the current workday,
        # then adding the remaining part to the next workday
        else:
            while not self.nextIsWorkday(due_date):
                due_date += timedelta(days=1)
            due_date += timedelta(days=1)
            remaining_minutes -= remaining_from_start_day
            due_date = datetime(due_date.year, due_date.month, due_date.day, self.startHour, 0)
            due_date += timedelta(minutes=remaining_minutes)

        return due_date
