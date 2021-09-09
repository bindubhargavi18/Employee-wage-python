import random

wage_per_hr = 20
full_day_hrs = 8
part_time_hrs = 4
emp_check = int(random.randint(0, 1))


def employee_attendance():
    if emp_check == 1:
        print("Employee is present")
    else:
        print("Employee is absent")


if __name__ == "__main__":
    employee_attendance()
