# # Question 4: Bank Customer Information System (Intermediate)

# ### Problem Statement

# A bank wants to display customer account information.

# Create a class named **BankCustomer**.

class BankCustomer:
    def __init__(self,Account_Number,Customer_Name ,Account_Type,Account_Balance):
        self.Account_Number = Account_Number
        self.Customer_Name = Customer_Name
        self.Account_Type = Account_Type
        self.Account_Balance = Account_Balance

    def display_Customer(self):
        print("-------------------------------------------")
        print("      Customer Details            ")
        print("--------------------------------------------")
        print(f"Account Number   : {self.Account_Number}")
        print(f"Customer Name    : {self.Customer_Name}")
        print(f"Account Type     : {self.Account_Type}")
        # print(f"Account Balance  : {self.Account_Balance}")

    def check_balance(self):
        print(f"Balance          : {self.Account_Balance}")

c1 = BankCustomer(12345678,"Ram","Savings",85000)
c1.display_Customer()
c1.check_balance()

c2 = BankCustomer(12346240,"Anil","Saving",50000)
c2.display_Customer()
c2.check_balance()

c3 = BankCustomer(12346240,"Lokesh","Open",40000)
c3.display_Customer()
c3.check_balance()

c4 = BankCustomer(52346240,"Ramesh","Regular",90000)
c4.display_Customer()
c4.check_balance()

# The class should store the following information:

# * Account Number
# * Customer Name
# * Account Type
# * Account Balance

# Create the following methods:

# * **display_customer()**
# * **check_balance()**

# ### Requirements

# * Create **4 BankCustomer objects**.
# * Display the customer details.
# * Display the available account balance.

# ### Expected Output Format

# ```
# ---------------------------------
# Customer Details
# ---------------------------------

# Customer Name   : Ram
# Account Number  : 12345678
# Account Type    : Savings
# Balance         : ₹85,000
# ```
