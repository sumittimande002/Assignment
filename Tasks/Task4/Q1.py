
## 31. Program to Check Palindrome String

# **Problem Statement:** Write a program to check whether a given string is a 
# palindrome (same forward and backward).

str = input("Enter a String : ")
if (str == str[::-1]):
    print("Given String is Palindrome.")
else:
    print("Given string is not Palindrome")