## 4. Program to Create an Employee Salary System

# **Problem Statement:** 
# Create an `Employee` class. The constructor should initialize employee name and basic salary.
#  Add a method to calculate salary after adding bonus (10%)


class Employee:
    def __init__(self,name,basic_salary):
        self.name = name
        self.basic_salary = basic_salary

    def clc_salary(self):
        updated = self.basic_salary + self.basic_salary/10
        print("Name : ",self.name)
        print("Final Salary :",updated)

e = Employee("Raju",1000)
e.clc_salary()
e2 = Employee("Ravi",20000)
e2.clc_salary()
e3 = Employee("Anu",5000)
e3.clc_salary()