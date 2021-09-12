import random

wage_per_hr = 20
total_working_days = 20
total_working_hrs = 100
full_time_hrs = 8
part_time_hrs = 4
absent_hrs = 0


class EmployeeWage:

    # def __init__(self, working_days, working_hrs):
    #     self.working_days = working_days
    #     self.working_hrs = working_hrs

    def wage_calculation(self):
        working_days = 0
        working_hrs = 0
        employee_check = int(input("Enter Employee Attendance type"))
        employee_attendance = {
            1: full_time_hrs,
            0: absent_hrs,
            2: part_time_hrs
        }

        try:
            while working_hrs <= total_working_hrs and working_days < total_working_days:
                # emp_check = int(random.randint(0, 2))
                working_hrs = working_hrs + employee_attendance.get(employee_check)
                working_days = working_days + 1
                total_wage = working_hrs * wage_per_hr
            print("total wage:", total_wage)
        except ValueError:
            print("Invalid input attendance type")


if __name__ == "__main__":
    employee = EmployeeWage()
    employee.wage_calculation()
