## 22. Program to Generate Multiplication Table

# **Problem Statement:** Write a program to generate the multiplication
#  table of a given number up to 10.
number = int(input("Enter Number : "))
for i in range(1,11):
    print(f"{number}*{i} : {number* i}")
