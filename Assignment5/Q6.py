# 6.Write a program to check whether a given string is a palindrome using string methods.

ch = input("Enter a String : ")

if ch == ch[::-1]:
    print("is Palindrome")
else:
    print("Not a Palindrome")



    # check rev str is same if same then is palindrome 