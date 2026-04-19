"""
6.Write a program to print a square pattern of stars of size N:

****
****       
****
****

and 

* * * *
* * * *       
* * * *
* * * *
"""

n = int(input("Enter a Number : "))
for i in range (1,n+1):
    print("*"*n)
print("===========================")
for j in range(0 , n):
    print(" * "*n)