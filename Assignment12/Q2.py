# # Question 2: Bank Account Management System

# ### Problem Statement

# A bank wants to securely manage customer accounts.

# Create a class named **BankAccount**.

class InsufficientBalanceError (Exception):
    pass

class NegativeBalanceError (Exception):
    pass

class BankAccount:

    Account_Number = int(input("Enter Account Number : "))
    Account_Holder_Name = input("Enter a Holder Name :")
    
    balance = int(input("Enter a balance : "))
    if balance <= 0:
        raise NegativeBalanceError("Enter a Positive Balance")
        

    def deposit(self,amount):
        self.balance += self.amount

    def withdraw(self,amount):
        if amount < self.balance :
            raise InsufficientBalanceError("Amount Shoud be greter then Balance.")
        else:
            self.balance -= amount

    def display_balance(self):
        print("Balance : ",self.balance)

    def bank_account_details(self):
        print("          Bank Account Details    ")

        print("Account Holder Name : ",self.Account_Holder_Name)
        print("Current Balance     : ",self.balance)
        print("Withdrawal          : ",self.withdraw)
        print("Remaining Balance   : ",self.balance)



b = BankAccount()

b.deposit(4000)
b.withdraw(400)
b.display_balance()
b.bank_account_details()







# Attributes:

# * Account Number
# * Account Holder
# * Balance

# Methods:
    

# * deposit()
# * withdraw()
# * display_balance()

# Handle the following exceptions:

# * Negative deposit amount
# * Withdrawal greater than available balance
# * Invalid numeric input

# ### Requirements

# * Raise a custom exception named **InsufficientBalanceError**.
# * Display meaningful error messages.
# * Ensure balance never becomes negative.

# ### Expected Output Format

# ```text
# -----------------------------------------
# Bank Account Details
# -----------------------------------------

# Account Holder    : Rahul

# Current Balance   : ₹50,000

# Withdrawal        : ₹10,000

# Remaining Balance : ₹40,000
# ```

    






# **Invalid Output**

# ```text
# Error: Insufficient balance.
# ```
