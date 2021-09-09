import random

wage_per_hr = 20
emp_check = int(random.randint(0, 2))


def employee_attendance():
    if emp_check == 1:
        print("Employee is present")
        full_day_hrs = 8
        emp_wage = full_day_hrs * wage_per_hr
    elif emp_check == 2:
        print("Employee worked as part-time")
        part_time_hrs = 4
        emp_wage = part_time_hrs * wage_per_hr
    else:
        print("Employee is absent")
        emp_wage = 0
    print("Employee wage is: ", emp_wage)


if __name__ == "__main__":
    employee_attendance()
