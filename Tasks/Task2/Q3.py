## 13. Program to Check Leap Year

# **Problem Statement:** Write a program to check whether a given year is a leap year.

year = int(input("Enter a year : "))
if(year% 2 == 0):
    print("Leap Year")
else:
    print("Not Leap Year")