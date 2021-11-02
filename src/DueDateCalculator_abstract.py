from abc import ABC, abstractmethod


class DueDateCalcAbstract(ABC):
    """ Abstract class for Due date Calculator """

    @abstractmethod
    def CalculateDueDate(self, submit_date, turnaround_time):
        raise NotImplementedError
