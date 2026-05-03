## 17. Program to Calculate Electricity Bill

# **Problem Statement:** Write a program to calculate electricity bill 
# based on units consumed.
# (Example logic: <100 Low, 100–200 Medium, >200 High)

units = int(input("Enter a Units : "))
if(units < 100):
    print("Low Bill ")
elif(units> 100 and units < 200):
    print("Medium Bill")
elif(units > 200):
    print("High Bill")