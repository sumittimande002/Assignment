## 20. Program to Find Sum of First N Numbers

# **Problem Statement:** Write a program to calculate the sum of first N
# natural numbers.

count = 0
sum = 0
number = int(input("Enter a Number : "))
for i in range(1,number+1):
    count += i
    # sum = sum + i
print(count)
# print(sum)