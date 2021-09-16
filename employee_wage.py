import random


class EmployeeWage:

    def __init__(self, wage_per_hr, working_days_in_month, working_hrs_in_month):
        self.wage_per_hr = wage_per_hr
        self.working_days_in_month = working_days_in_month
        self.working_hrs_in_month = working_hrs_in_month

    def employee_daily_wage(self, emp_work_hrs):
        return emp_work_hrs * self.wage_per_hr

    def employee_working_hrs(self, emp_check):
        full_time_hrs = 8
        part_time_hrs = 4
        absent_hrs = 0
        employee_attendance = {
            1: full_time_hrs,
            0: absent_hrs,
            2: part_time_hrs
        }
        return employee_attendance.get(emp_check)

    def employee_total_salary(self):
        working_days = 0
        total_working_hrs = 0
        total_wage = 0
        while total_working_hrs < self.working_hrs_in_month and working_days < self.working_days_in_month:
            emp_check = int(random.randint(0, 2))
            emp_hrs = EmployeeWage.employee_working_hrs(self, emp_check)
            total_working_hrs = total_working_hrs + emp_hrs
            working_days = working_days + 1
            total_wage = total_wage + self.employee_daily_wage(emp_hrs)

        return total_wage



