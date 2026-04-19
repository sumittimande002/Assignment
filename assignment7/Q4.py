# 4.Write a program to count the number of digits in a given number using a loop.

n = int(input("Enter a Number : "))
count = 0 
while n > 0:
    n = n// 10
    count += 1
print(count)