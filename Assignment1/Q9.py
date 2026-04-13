# 9. Next Multiple of 100
# Problem Statement: Write a program to find the next multiple of 100 greater than
#  a given number. The program should take a number as input and output the next
#  multiple of 100.

number = int(input("Enter a Number : "))
res = 100*(int(number/100)+1)
print("Next Multiple of 100 is : " ,res)