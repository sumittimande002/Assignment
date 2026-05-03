## 24. Program to Count Digits in a Number

# **Problem Statement:** Write a program to count the number of digits 
# in a given number.


number = int(input("Enter Number : "))
count = 0
if number == 0 :
    print("1")
else:
    while number != 0:
        number = number // 10
        count += 1
    print(count)
    