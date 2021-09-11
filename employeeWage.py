import random

wage_per_hr = 20
full_day_hrs = 8
part_time_hrs = 4
emp_check = int(random.randint(0, 2))


def is_full_time():
    return "Full-Time Employee wage is: ", full_day_hrs * wage_per_hr


def is_part_time():
    return "Part- Time Employee wage is: ", part_time_hrs * wage_per_hr


def is_absent():
    return "Employee is absent: wage is 0"


def default():
    return "Invalid choice"


employee_wage = {
    0: is_absent,
    1: is_part_time,
    2: is_full_time
}
if __name__ == "__main__":
    result = employee_wage.get(emp_check, default)()
    print(result)
