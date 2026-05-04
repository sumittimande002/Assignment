## 25. Program to Generate Fibonacci Series

# **Problem Statement:** Write a program to generate Fibonacci series up to N terms.
num  = int(input("Enter Number : "))
# a , b = 0,1
# for i in range (a,num):
#     print(a , end=" ")
#     c = a+b
#     a = b
#     b = c
#     # a , b = b ,a+b










a , b = 0,1

for i in range (a,num):
    print(a, end = " ")
    c = a+ b
    a = b
    b = c