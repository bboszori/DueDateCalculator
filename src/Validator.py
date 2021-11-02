from datetime import datetime


class Validator:
    """ A class for validating inputs for DueDateCalculator. """

    @staticmethod
    def isSubmitDateValid(submit_date):
        """ Returns True if submit_date's type is datetime """
        return isinstance(submit_date, datetime)

    @staticmethod
    def isWorkday(submit_date):
        """ Returns True if submit_date is workday """
        return datetime.weekday(submit_date) < 5

    @staticmethod
    def isWithinWorkingHours(submit_date, start_time, end_time):
        """ Returns True if submit_date's time is in working hours """
        return start_time <= submit_date.hour < end_time

    def isInServiceTime(self, submit_date, start_time, end_time):
        """ Returns True if submit_date is on a workday and in the working hours """
        return self.isWorkday(submit_date) and self.isWithinWorkingHours(submit_date, start_time, end_time)

    @staticmethod
    def isTurnaroundTimeValid(ta_Time):
        """ Returns True ta_time is a non-negative int or float """
        return (isinstance(ta_Time, int) or isinstance(ta_Time, float)) and ta_Time >= 0
