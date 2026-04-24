# 6.Write a program to reverse a number using a while loop.

num = 1234
i = 0
while num > 0:
    digit = num % 10       
    i = i * 10 + digit 
    num = num // 10 
print("Reverse no is : ",num)

