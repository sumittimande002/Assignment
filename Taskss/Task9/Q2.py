# # Question 2: Employee Payroll System (Protected Members)

# ### Problem Statement

# A company wants salary information to be accessible only within the class and its child classes.

# Create a **Parent Class** named **Employee**.

# Create the following **Protected Attributes**:

# * _employee_id
# * _employee_name
# * _salary

class Employee:
    def __init__(self,employee_id,employee_name,salary):
        self._employee_id = employee_id
        self._employee_name = employee_name
        self._salary = salary


# Create a protected method:

# * _display_employee()

    def _display_employee(self):
        print("-------------------------------")
        print("       Employee Details  ")
        print("-------------------------------")
        print(f"Employee ID   : {self._employee_id}")
        print(f"Employee Name : {self._employee_name}")
        print(f"Salary        : {self._salary}")

# Create a **Child Class** named **Manager**.

# Create a public method:

class Manager(Employee):
    def display_manager_details(self):
        self._display_employee()
        print("Designation   : Manager")


m = Manager(101,"Sumit",8000000)
m.display_manager_details()

# * display_manager_details()

# which accesses the protected members.

# ### Requirements

# * Demonstrate access to protected members using inheritance.
# * Display employee details from the child class.

# ### Expected Output Format

# ```text
# -----------------------------------------
# Employee Details
# -----------------------------------------

# Employee ID      : EMP101
# Employee Name    : Rahul Sharma
# Salary           : ₹75,000
# Designation      : Manager
