#  Question 3: Employee Payroll Security System (Intermediate)

# ### Problem Statement

# A company wants to keep employee salaries confidential.

# Create a class named **Employee**.

# Store:

# * Employee ID
# * Employee Name
# * Department
# * Private Variable: **Salary**

class Employee:
    def __init__(self, emp_id, emp_name, department, salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.department = department
        if salary >= 15000:
            self.__salary = salary 
        else:
            print("Salary cannot be less than ₹15,000.")  
    

    def set_salary(self ,salary):
        self.__salary += salary
    
    def get_salary(self,salary):
        if salary >= 15000:
            self.__salary = salary
        else:
            print("Salary cannot be less than ₹15,000.")
        

    def display_employee(self):
        print("-----------------------------------------")
        print("      Employee Details")
        print("-----------------------------------------")
        print(f"Emp ID         : {self.emp_id}")
        print(f"Employee Name  : {self.emp_name}")
        print(f"Department     : {self.department}")
        print(f"Salary         : {self.__salary}")


e1 = Employee(101,"Sumit","IT",25000)
e2 = Employee(102,"Sumi","IT",25000)
e3 = Employee(103,"Sumit","IT",25000)
e4 = Employee(104,"Sumit","IT",25000)
e5 = Employee(105,"Sumit","IT",25000)

e1.display_employee()
e2.display_employee()
e3.display_employee()
e4.display_employee()
e5.display_employee()
# Create the following methods:

# * **set_salary()**
# * **get_salary()**
# * **display_employee()**

# Validation Rule:

# * Salary cannot be less than ₹15,000.
# * If an invalid salary is entered, display an appropriate message.

# ### Requirements

# * Create **5 Employee objects**.
# * Validate salary before storing it.
# * Display employee details using methods.

# ### Expected Output Format

# ```text
# -----------------------------------------
# Employee Details
# -----------------------------------------

# Employee ID      : 1001
# Employee Name    : Priya
# Department       : Python

# Salary           : ₹50,000