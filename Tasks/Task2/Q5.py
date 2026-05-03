## 15. Program to Check Palindrome Number

# **Problem Statement:** Write a program to check whether a number is a palindrome.

num = int(input("Enter a Number : "))
# if(num == num[::-1]):
#     print("Palindrome")
# else:
#     print("Not a Palindrome")

original_value = num
rev = 0
while num > 0 :
    digit = num % 10
    rev = rev *10 + digit
    num = num // 10
if original_value == rev :
    print("Palindrome")
else:
    print("Not Palindrome")


