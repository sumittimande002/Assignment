# # Question 2: Employee Information System (Beginner)

# ### Problem Statement

# An IT company wants to maintain employee information.

# Create a class named **Employee**.

class Employee:
    Company_Name = "Tech Solutions Pvt Ltd"

    def __init__(self,Employee_ID,Employee_Name,Department,Salary):
        self.Employee_ID = Employee_ID
        self.Employee_Name = Employee_Name
        self.Department = Department
        self.Salary = Salary

    def display_employee(self):
        Bonus = 5000
        print("----------------------------------------")
        print("         Employee Details")
        print("----------------------------------------")
        print(f"Company Name      : {self.Company_Name}")
        print(f"Employee Name     : {self.Employee_Name}")
        print(f"Department        : {self.Department}")
        print(f"Salary            : {self.Salary}")
        print(F"Bonus             : {Bonus}")


e1 = Employee(101,"Sumit","Python Developement",25000)
e1.display_employee()

e2 = Employee(102,"Rahul","Java Developement",50000)
e2.display_employee()

e3 = Employee(103,"Rajuu","JS Developement",80000)
e3.display_employee()

e4 = Employee(104,"Sumi","Python Developement",35000)
e4.display_employee()

# Use:

# ### Instance Variables

# * Employee ID
# * Employee Name
# * Department
# * Salary

# ### Class Variable

# * Company Name = "Tech Solutions Pvt Ltd"

# Create a method named **display_employee()**.

# Inside the method, create a **Local Variable** named:

# ```text
# Bonus = 5000
# ```

# Display:

# * Employee Details
# * Company Name
# * Bonus

# ### Requirements

# * Create **4 Employee objects**.
# * Display all employee details.


