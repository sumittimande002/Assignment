# 3.Write a program to calculate the sum of first N natural numbers using a while loop.

n = int(input("Enter a Number : "))
total = 0
i = 1
while i <= n:
    total = total + i
    i = i + 1

print(f"Sum of {n} natural number is : {total}")
