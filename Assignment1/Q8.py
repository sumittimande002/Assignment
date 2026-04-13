# 8. Swap Two Numbers
# Problem Statement: Write a program to swap two numbers without using a third
#  variable. The program should take two numbers as input and swap their values.

a , b = int(input("Enter a 1st Number : ")) ,int(input("Enter a 2nd Number : "))

a , b = b , a
print("Value of a is : ",a)
print("Value of b is : ",b)