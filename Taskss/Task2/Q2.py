# # Question 2: Employee Salary System (Beginner)

# ### Problem Statement

# An IT company wants to store employee information during object creation.

# Create a class named **Employee**.
class Employee:
    def __init__(self,Employee_ID,Employee_Name,Department,Basic_Salary):
        self.Employee_ID = Employee_ID
        self.Employee_Name = Employee_Name
        self.Department = Department
        self.Basic_Salary = Basic_Salary

    def display_employee(self):
        print("--------------------------------------")
        print("          Employee Details   ")
        print("--------------------------------------")
        print(f"Employee ID      : {self.Employee_ID}")
        print(f"Employee Name    : {self.Employee_Name}")
        print(f"Department       : {self.Department}")
        print(f"Basic Salary     : {self.Basic_Salary}")

    def annual_salary(self):
        total_salary = self.Basic_Salary * 12
        print(f"Annual Salary    : {total_salary}")

e1 = Employee(101,"Sumit","IT",15000)
e1.display_employee()
e1.annual_salary()
e2 = Employee(102,"Rajesh","CSE",18000)
e2.display_employee()
e2.annual_salary()

e3 = Employee(103,"Rajuu","CSE",15000)
e3.display_employee()
e3.annual_salary()

e4 = Employee(104,"Gagan","EXE",13000)
e4.display_employee()
e4.annual_salary()

e5 = Employee(105,"Gunjan","LM",19000)
e5.display_employee()
e5.annual_salary()



# Initialize the following information using the constructor:

# * Employee ID
# * Employee Name
# * Department
# * Basic Salary

# Create the following methods:

# * **display_employee()**
# * **annual_salary()**

# The annual salary should be calculated as:

# ```text
# Annual Salary = Basic Salary × 12
# ```

# ### Requirements

# * Create **5 Employee objects**.
# * Display employee details.
# * Display the annual salary of each employee.

# ### Expected Output Format

# ```text
# -----------------------------------------
# Employee Details
# -----------------------------------------

# Employee ID     : 1001
# Employee Name   : Sairam
# Department      : Python
# Basic Salary    : ₹50,000

# Annual Salary   : ₹6,00,000
# ```
