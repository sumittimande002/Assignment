## 14. Program to Simulate ATM Withdrawal

# **Problem Statement:** Write a program to simulate ATM withdrawal. 
# Check if the withdrawal amount is less than or equal to balance.

balance = int(input("Enter a Balance : "))
withdrawal = int(input("Enter a Withdrawal amount : "))

if (balance >= withdrawal):
    print("Transaction Successful.")
else :
    print("Insufficient Balance")