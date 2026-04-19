# 2.Write a program to find the sum of all even numbers between 1 and N using a loop.

n = int(input("Enter a Number : "))
total = 0

for i in range (1,n+1):
    if i % 2 == 0 :
        total = i + total 

print(total)
