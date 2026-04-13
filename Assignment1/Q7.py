# Program to Find the Maximum of Two Numbers Using Ternary Operator
# Problem Statement: Write a program to find the maximum of two numbers using
# the ternary operator. The program should take two numbers as input and 
# output the larger of the two.
a = int (input("Enter a 1st Number : "))
b = int (input("Enter a 2nd Number : "))

if(a>b):
    print("A is Large Number and Value of A is :",a)
elif(a<b):
    print("B is Large and value of B is : ",b)
elif(a==b):
    print("A and B is Equal and Value is : ",a)
