# Employee Attendance System (Beginner)

# ### Problem Statement

# A software company wants to calculate the working hours of different types of employees.

# Create an **Abstract Class** named **Employee**
from abc import ABC,abstractmethod
class Employee(ABC):
    @abstractmethod
    def calculate_salary():
        pass
    @abstractmethod
    def working_hours():
       pass


class FullTimeEmployee(Employee):
    def calculate_salary(self,salary):
        print("----------------------------")
        print("       Employee Details  ")
        print("----------------------------")
        print("Employee Type  : Full Type")
        print("Salary         : ",salary)

    def working_hours(self,hr):
        print("Working Hours  : ",hr)


class PartTimeEmployee(Employee):
    def calculate_salary(self,salary):
        print("----------------------------")
        print("       Employee Details  ")
        print("----------------------------")
        print("EMployee Type  : Part Type")
        print("Salary         : ",salary)

    def working_hours(self,hr):
        print("Working Hours  : ",hr)


class ContractEmployee:
    def calculate_salary(self,salary):
        print("----------------------------")
        print("       Employee Details  ")
        print("----------------------------")
        print("Employee Type  : Contract Type")
        print("Salary         : ",salary)

    def working_hours(self,hr):
        print("Working Hours  : ",hr)


f = FullTimeEmployee()
p = PartTimeEmployee()
c = ContractEmployee()
f.calculate_salary(80000)
f.working_hours(8)
p.calculate_salary(40000)
p.working_hours(6)
c.calculate_salary(90000)
c.working_hours(7)

# Create the following abstract methods:

# * calculate_salary()
# * working_hours()

# Create the following child classes:

# * FullTimeEmployee
# * PartTimeEmployee
# * ContractEmployee

# Each employee type should calculate salary differently.

# ### Requirements

# * Create one object for each employee type.
# * Display working hours.
# * Display salary calculation.

# ### Expected Output Format

# ```text
# -----------------------------------------
# Employee Details
# -----------------------------------------

# Employee Type      : Full Time
# Working Hours      : 8 Hours
# Monthly Salary     : ₹55,000

# -----------------------------------------

# Employee Type      : Part Time
# Working Hours      : 4 Hours
# Monthly Salary     : ₹22,000
# ```
