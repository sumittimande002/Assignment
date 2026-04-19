# 10.Write a program to find the factorial of a given number using a loop.

n = int(input("Enter a Number : "))
total = 1
for i in range(1,n+1):
    total = i *total
print(total)