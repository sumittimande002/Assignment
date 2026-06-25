# # Question 1: Employee Management System (Single Inheritance)

# ### Problem Statement

# A software company wants to maintain employee information.

# Create a **Parent Class** named **Employee** with the following attributes:

# * Employee ID
# * Employee Name
# * Department

class Employee:
    def __init__(self,Employee_ID,Employee_Name,Department):
        self.Employee_ID = Employee_ID
        self.Employee_Name = Employee_Name
        self.Department = Department

    def employee_details(self):
        print("-----------------------------------------")
        print("         Employee Details")
        print("------------------------------------------")
        print(f"Employee ID        : {self.Employee_ID}")
        print(f"Employee Name      : {self.Employee_Name}")
        print(f"Department         : {self.Department}")

class Developer(Employee):
    def __init__(self,Employee_ID, Employee_Name, Department, Programming_Language, Exprince, Salary):
        super().__init__(Employee_ID, Employee_Name, Department)
        self.Programming_Language = Programming_Language
        self.Exprince = Exprince
        self.Salary = Salary
        
    def developer_details(self):
        self.employee_details()
        print(f"Programming Lang   : {self.Programming_Language}")
        print(f"Experience         : {self.Exprince} Years")
        print(f"Salary             : {self.Salary}")


e = Developer("EMP101", "Rahul Sharma", "Information Technology", "Python", 4, "8,50,000")
e.developer_details()



# Create a method named:

# * employee_details()

# Create a **Child Class** named **Developer** with the following additional attributes:

# * Programming Language
# * Experience
# * Salary

# Create a method named:

# * developer_details()

# ### Requirements

# * Accept employee details.
# * Display both employee and developer information.
# * Use the `super()` method to initialize parent class attributes.

# ### Expected Output Format

# ```text
# -----------------------------------------
# Employee Details
# -----------------------------------------

# Employee ID        : EMP101
# Employee Name      : Rahul Sharma
# Department         : Information Technology

# Programming Lang.  : Python
# Experience         : 4 Years
# Salary             : ₹8,50,000
