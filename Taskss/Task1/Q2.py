# # Question 2: Employee ID Card Generator (Beginner)

# ### Problem Statement

# An IT company wants to generate employee ID cards.

# Create a class named **Employee**.

class Employee:
    def __init__(self,Employee_ID,Employee_Name,Department,Salary):
        self.Employee_ID = Employee_ID
        self.Employee_Name = Employee_Name
        self.Department = Department
        self.Salary = Salary


    def generate_id_card(self):
        print("---------------------------------")
        print("   Employee ID Card    ")
        print("---------------------------------")
        print(f"Employee Id   : {self.Employee_ID}")
        print(f"Employee Name : {self.Employee_Name}")
        print(f"Department    : {self.Department}")
        print(f"Salary        : {self.Salary}")
        print("----------------------------------")


E1 = Employee(10001,"Sairam","Python",50000)
E1.generate_id_card()
E2 = Employee(10002,"Sumit","Python",20000)
E2.generate_id_card()
E3 = Employee(10003,"Rahul","JS",30000)
E3.generate_id_card()
E4 = Employee(10004,"Ram","Python",40000)
E4.generate_id_card()
E5 = Employee(10005,"Sai","Java",20000)
E5.generate_id_card()

# The class should store the following information:

# * Employee ID
# * Employee Name
# * Department
# * Salary

# Create a method named **generate_id_card()** to display the employee details.

# ### Requirements

# * Create **5 Employee objects**.
# * Display the ID card of every employee.

# ### Expected Output Format

# ```
# ---------------------------------
# EMPLOYEE ID CARD
# ---------------------------------

# Employee ID     : 1001
# Employee Name   : Sairam
# Department      : Python
# Salary          : ₹50,000

