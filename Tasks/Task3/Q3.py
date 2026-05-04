## 23. Program to Reverse a Number

# **Problem Statement:** Write a program to reverse the digits of a number.
num = int(input("Enter a Number : "))

# while num != 0:
#    dig = num % 10 
#    new = dig
#    num = num // 10
#    print(new ,end="")


while num!= 0:
    dig = num % 10
    new = dig
    num = num // 10
    print(new,end="")