import random

wage_per_hr = 20
emp_check = int(random.randint(0, 1))


def employee_attendance():
    if emp_check == 1:
        print("Employee is present")
        full_day_hrs = 8
    else:
        print("Employee is absent")
        full_day_hrs = 0
    emp_wage = full_day_hrs * wage_per_hr
    print("Employee wage is: ", emp_wage)


if __name__ == "__main__":
    employee_attendance()
