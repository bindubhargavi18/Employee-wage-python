from employee_wage import EmployeeWage


class CompanyWage(EmployeeWage):

    def __init__(self, no_of_employees, company_name, wage_per_hr, working_days_in_month, working_hrs_in_month):
        super().__init__(wage_per_hr, working_days_in_month, working_hrs_in_month)
        self.no_of_employees = no_of_employees
        self.company_name = company_name

    def company_employee_wages(self):
        employee_wages = []
        for i in range(0, self.no_of_employees, 1):
            employee_wages.append(EmployeeWage.employee_total_salary(self))
        return employee_wages

    def company_total_wage(self):
        try:
            if self.working_days_in_month < 1 or self.working_days_in_month > 29:
                raise DaysNotValidException(self.company_name)
            else:
                total_company_wage = self.company_employee_wages()
                print("Each employee wage in company {}:".format(self.company_name))
                print(total_company_wage)
                print("Total wage of company {}:".format(self.company_name))
                print(sum(total_company_wage))

        except DaysNotValidException as e:
            print("Working days in month for company {} is not valid.. Please give valid days..".format(e))

        except ValueError:
            print("Data given is not valid type.. Enter only integer type..")


class DaysNotValidException(Exception):
    def __init__(self, message):
        self.message = message


if __name__ == "__main__":
    company = CompanyWage(10, "AMAZON", 20, 7, 100)
    company.company_total_wage()
    company1 = CompanyWage(5, "APPLE", 40, 25, 150)
    company1.company_total_wage()
