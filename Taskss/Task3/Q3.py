# Question 3: Bank Customer Management System (Intermediate)

# ### Problem Statement

# A bank wants to manage customer accounts.

# Declare a **Global Variable**

# ```python
# BANK_NAME = "National Bank of India"
# ```

# Create a class named **Customer**.

class Customer:
    BANK_NAME = "National Bank of India"

    def __init__(self,Account_Number, Customer_Name,Account_Type,Balance):
        self.Account_Number = Account_Number
        self.Customer_Name = Customer_Name
        self.Account_Type = Account_Type
        self.Balance = Balance


    def display_account(self):
        print("----------------------------------------")
        print("          Customer Details")
        print("----------------------------------------")
        print(f"Bank Name         : {self.BANK_NAME}")
        print(f"Account Number    : {self.Account_Number}")
        print(f"Customer Name     : {self.Customer_Name}")
        print(f"Account Type      : {self.Account_Type}")
        print(f"Balance           : {self.Balance}")


c1 = Customer(1010101040,"Rahul","Free",50000)
c1.display_account()

c2 = Customer(1110101040,"Kunal","Free",60000)
c2.display_account()

c3 = Customer(21010101040,"Rushii","Free",60000)
c3.display_account()

c4 = Customer(3510101040,"Vihan","Free",80000)
c4.display_account()

c5 = Customer(5010101040,"Ayshuu","Open",55000)
c5.display_account()

# Use:

# ### Instance Variables

# * Account Number
# * Customer Name
# * Account Type
# * Balance

# Create a method named **display_account()**.

# Display:

# * Bank Name (Global Variable)
# * Customer Details
# * Available Balance

# ### Requirements

# * Create **5 Customer objects**.
# * Display all customer account information.

# ### Expected Output Format

# ```text
# -----------------------------------------
# Bank Customer Details
# -----------------------------------------

# Bank Name       : National Bank of India

# Account Number  : 12345678
# Customer Name   : Priya
# Account Type    : Savings
# Balance         : ₹85,000
# ``