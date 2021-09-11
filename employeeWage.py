import random

wage_per_hr = 20
total_working_days = 20
total_working_hrs = 100
full_time_hrs = 8
part_time_hrs = 4
absent_hrs = 0


def wage_calculation():
    working_days = 0
    working_hrs = 0
    employee_attendance = {
        1: full_time_hrs,
        2: part_time_hrs,
        0: absent_hrs
    }
    while working_hrs <= total_working_hrs and working_days < total_working_days:
        emp_check = int(random.randint(0, 2))
        working_hrs = working_hrs + employee_attendance.get(emp_check)
        working_days = working_days + 1
        total_wage = working_hrs * wage_per_hr

    return total_wage


if __name__ == "__main__":
    print("Monthly wage: ", wage_calculation())
