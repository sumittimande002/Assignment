# Question 2: Employee Payroll System (Beginner)

# ### Problem Statement

# A software company wants to generate employee salary reports.

# Create a class named **Employee**.

class Employee:
    def __init__(self,Employee_ID,Employee_Name,Department,Salary):
        self.Employee_ID = Employee_ID
        self.Employee_Name = Employee_Name
        self.Department = Department
        self.Salary = Salary

    def display_Employee(self):
        print(f"Employee ID      : {self.Employee_ID}")
        print(f"Employee Name    : {self.Employee_Name}")
        print(f"Department       : {self.Department}")
        print(f"Salary           : {self.Salary}")
    

    def Annual_Salary(self):
        total_salary = 12 * self.Salary
        print(f"Annual Salary    : {total_salary}")

    def company_name(self):
        print("-------------------------------------")
        print("       Employee Details   ")
        print("-------------------------------------")
        print("       Tech Solution")

    @staticmethod
    def working_days():
        print(f"Working Days is 22")


e1 = Employee(1001,"Rajesh","IT",50000)
e1.company_name()
e1.display_Employee()
e1.Annual_Salary()
e1.working_days()

e2 = Employee(1001,"Rajesh","IT",50000)
e2.company_name()
e2.display_Employee()
e2.Annual_Salary()
e2.working_days()

e3 = Employee(1001,"Rajesh","IT",50000)
e3.company_name()
e3.display_Employee()
e3.Annual_Salary()
e3.working_days()

e4 = Employee(1001,"Rajesh","IT",50000)
e4.company_name()
e4.display_Employee()
e4.Annual_Salary()
e4.working_days()

e5 = Employee(1001,"Rajesh","IT",50000)
e5.company_name()
e5.display_Employee()
e5.Annual_Salary()
e5.working_days()
# Store:

# * Employee ID
# * Employee Name
# * Department
# * Salary

# Create the following methods.

# ### Instance Method

# **display_employee()**

# Display employee information.

# ### Instance Method

# **annual_salary()**

# Calculate

# ```text
# Annual Salary = Monthly Salary × 12
# ```

# ### Class Method

# **company_name()**

# Display

# ```text
# Tech Solutions Pvt Ltd
# ```

# ### Static Method

# **working_days()**

# Display

# ```text
# Working Days Per Month : 22
# ```

# ### Requirements

# * Create **5 Employee objects**.
# * Call every method.
