# Program to Calculate Simple Interest
# Problem Statement: Write a program to calculate the simple interest. The program should take the
# principal amount, rate of interest, and time in years as input, and calculate the simple interest

principal = int (input("Enter a Principal Amount : "))
intrest = int(input("Enter a Rate of Intrest : "))
time = int (input("Enter a Time in Years : "))

SI =  (principal * intrest * time)/100

print("Simple Intrest is : " ,int(SI))
