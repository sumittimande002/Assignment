## 18. Program to Apply Discount

# **Problem Statement:** Write a program to apply discount based on purchase amount.
# (>1000 → 10%, 500–1000 → 5%, <500 → No discount)


amount = int(input("Enter a Amount : "))
if(amount > 1000):
    amount / 10
    print("10% Discount")
elif(amount< 1000 and amount > 500):
    print("5% Discount")
elif(amount<500):
    print("No Discount")
    