
## 28. Program to Find Sum of Digits

# **Problem Statement:** Write a program to calculate the sum of digits of a number.

num = int(input("Enter a Number : "))
sum = 0
while(num != 0):
    dig = num % 10 #last number
    sum = sum + dig  #add
    num = num // 10 #remove

print(sum)