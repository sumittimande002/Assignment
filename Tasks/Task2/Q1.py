## 11. Program to Check Divisibility by 3 and 5

# **Problem Statement:** Write a program to check whether a number is divisible by both 3 and 5.
num = int(input("Enter a Number : "))
if(num%3 == 0 and num % 5 == 0):
    print("Number is Divisible by 3 and 5")
else:
    print("Not Divisible both")