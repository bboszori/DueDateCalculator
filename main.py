from datetime import datetime
from src.DueDateCalculator import DueDateCalculator


def main():
    due_date_calc = DueDateCalculator()
    submit_date = datetime(2021, 11, 2, 15, 32)
    turnaround_time = 47
    due_date = due_date_calc.CalculateDueDate(submit_date, turnaround_time)
    print(due_date)


if __name__ == '__main__':
    main()
