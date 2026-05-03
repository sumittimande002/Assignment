## 12. Program to Validate Login Credentials

# **Problem Statement:** Write a program to validate a username and password
# entered by the user. Assume correct credentials are username = "admin" 
# and password = "1234".

username = input("Enter a User Name : ")
password = input("Enter a Password : ")
if(username == "admin" and password == "1234"):
    print("Login Successful.")
else:
    print("Invalid Credentials")