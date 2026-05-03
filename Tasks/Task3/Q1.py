## 21. Program to Calculate Factorial of a Number

# **Problem Statement:** Write a program to calculate the factorial of a given number using a loop.

number = int(input("Enter a Number : "))
count = 1
if number ==  0 or number == 1:
    print("1")
else:
    for i in range(2,number+1):
        count *= i

    print(count)
