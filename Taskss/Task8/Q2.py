# # Question 2: Employee Salary Management (Method Overriding)

# ### Problem Statement

# A company calculates salaries differently for different employee categories.

# Create a **Parent Class** named **Employee** with the method:

# * calculate_salary()

class Employee:
    def calculate_salary(self):
        pass


class FullTimeEmployee(Employee):
    def calculate_salary(self,Salary):
        print("-----------------------------")
        print("    Employee Salary Details ")
        print("-------------------------------")
        print("Type      : Full Time Employee")
        print(f"Salary    : {Salary}")

class PartTimeEmployee(Employee):
    def calculate_salary(self,Salary):
        print("--------------------------------")
        print("Type      : Part Time Employee")
        print(f"Salary    : {Salary}")


class ContractEmployee(Employee):
    def calculate_salary(self,Salary):
        print("-------------------------------")
        print("Type      : Contract Employee")
        print(f"Salary    : {Salary}")



f = FullTimeEmployee()
f.calculate_salary(80000)

p = PartTimeEmployee()
p.calculate_salary(40000)

c = ContractEmployee()
c.calculate_salary(6000)

# Create the following child classes:

# * FullTimeEmployee
# * PartTimeEmployee
# * ContractEmployee

# Each class should override the salary calculation.

# ### Requirements

# * Create one object for each employee type.
# * Call the same method for all objects.
# * Display salary details.

# ### Expected Output Format

# ```text
# -----------------------------------------
# Employee Salary Details
# -----------------------------------------

# Employee Type      : Full Time
# Salary             : ₹60,000

# -----------------------------------------

# Employee Type      : Part Time
# Salary             : ₹25,000

# -----------------------------------------

# Employee Type      : Contract
# Salary             : ₹40,000
# ```
