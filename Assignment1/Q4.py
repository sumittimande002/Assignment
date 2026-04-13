# Program to Calculate Total Salary
# Problem Statement: Write a program to calculate the total salary of an employee.
# The program should take the basic salary, House Rent Allowance (HRA), and Dearness Allowance (DA)
# as input and calculate the total salary.
basic_salary = int(input("Enter a Basic Salary : "))
HRA = int(input("Enter a House Rent Allowance : "))
DA = int(input("Enter a Dearness Allowance : " ))

total_salary = basic_salary + HRA + DA
print("Total Salary of Employee : ",total_salary)

