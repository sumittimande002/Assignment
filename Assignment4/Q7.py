# 7.What is the difference between == and is operators?
# Write a program to prove it.
a = int(input("Enter a Number : "))
b = int(input("Enter a Number : "))
l1 = [10,20,30]
l2 = [10,20,30]
print("-------- == Compare value --------")
print(a == b)
print(l1 == l2)
print("-------- is Compare Object --------")
print(l1 is l2)