# DueDateCalculator

A due date calculator solution.
* It receives the submit date/time and turnaround time as inputs.
* And returns with the date/time when the issue is resolved.

The project is implemented in python3.

## Usage

The solution can be run with the command 
`python3 main.py` 

It creates an instance of DueDateCalculator. The start and end of the workday can be given there. The default values are 9 and 17.

To calculate the due date, the CalculateDueDate method has to be run.
The parameters are:
   1. submit_date - type: datetime, must be within working hours.
   2. turnaround_time - must be a non-negative number
 
It returns with the calculated due date in datetime format.

## Testing
The solution was implemented with test-driven concept. 

The test cases can be found in the DueDateCalculator/test directory.
