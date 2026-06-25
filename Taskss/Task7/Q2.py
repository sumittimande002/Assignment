# # Question 2: Banking System (Multilevel Inheritance)

# ### Problem Statement

# A bank wants to maintain customer, account, and loan information.

# Create the following classes:

# **Parent Class**

# Customer

# Attributes:

# * Customer ID
# * Customer Name

class Customer:
    def __init__(self,Customer_ID,Customer_Name):
        self.Customer_ID = Customer_ID
        self.Customer_Name = Customer_Name

    def customer_details(self):
        print("----------------------------------------")
        print("          Customer Details    ")
        print("----------------------------------------")
        print(f"Customer ID    : {self.Customer_ID}")
        print(f"Customer Name  : {self.Customer_Name}")


class Account(Customer):
    def __init__(self,Customer_ID,Customer_Name,Account_Number,Account_Type,Balance):
        super().__init__(Customer_ID,Customer_Name)
        self.Account_Number = Account_Number
        self.Account_Type = Account_Type
        self.Balance = Balance


    def account_details(self):
        
        print(f"Account Number : {self.Account_Number}")
        print(f"Account_Type   : {self.Account_Type}")
        print(f"Balance        : {self.Balance}")



# Methods:

# * customer_details()

# **Child Class**

# Account

# Additional Attributes:

# * Account Number
# * Account Type
# * Balance

# Method:

# * account_details()

# **Grandchild Class**

class Loan(Account):
    def __init__(self,Customer_ID,Customer_Name,Account_Number,Account_Type,Balance,Loan_Amount,Interest_Rate):
        super().__init__ (Customer_ID,Customer_Name,Account_Number,Account_Type,Balance)
        self.Loan_Amount = Loan_Amount
        self.Interest_Rate = Interest_Rate
        self.Balance = Balance

    def loan_deteils(self):
        self.customer_details()
        self.account_details()
        print(f"Loan Amount    : {self.Loan_Amount}")
        print(f"Interest Rate  : {self.Interest_Rate}")
        print(f"Balance        : {self.Balance}")

l = Loan("ID1000024","Rahul",10002445,"Saving",50002,40000,2)
l.loan_deteils()

# Loan

# Additional Attributes:

# * Loan Amount
# * Interest Rate

# Method:

# * loan_details()

# ### Requirements

# * Demonstrate **Multilevel Inheritance**.
# * Display customer, account, and loan details.

# ### Expected Output Format

# ```text
# -----------------------------------------
# Customer Details
# -----------------------------------------

# Customer ID      : C101
# Customer Name    : Sai Ram

# Account Number   : 2345678901
# Account Type     : Savings
# Balance          : ₹75,000

# Loan Amount      : ₹5,00,000
# Interest Rate    : 9%
# ```
