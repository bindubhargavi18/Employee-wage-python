import random

wage_per_hr = 20
working_days_in_month = 20
is_full_time = 1
is_part_time = 2


def wage_calculation():
    for day in range(0, 20, 1):
        monthly_wage = 0
        emp_check = int(random.randint(0, 2))
        if emp_check == 1:
            emp_hrs = 8
        elif emp_check == 2:
            emp_hrs = 4
        else:
            emp_hrs = 0

        emp_wage = emp_hrs * wage_per_hr
        monthly_wage = monthly_wage + emp_wage
        print("emp_wage", emp_wage)

    return monthly_wage


if __name__ == "__main__":
    print("Monthly wage", wage_calculation())
