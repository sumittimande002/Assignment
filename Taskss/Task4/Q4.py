# # Question 4: Bank Account Management System (Intermediate)

# ### Problem Statement

# A bank wants to automate customer account management.

# Create a class named **BankAccount**.

class BankAccount:
    def __init__(self, account_number, customer_name, balance):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance

    def display_account(self):
        print("-------------------------------------")
        print("       Account Details   ")
        print("-------------------------------------")
        print(f"Account Number   : {self.account_number}")
        print(f"Customer Name    : {self.customer_name}")
        print(f"Balance          : {self.balance}")
    
    def deposit(self, amount):
        self.balance+= amount
        print(f"Deposit          : {self.balance}")

    def withdraw(self,amount):
        self.balance -= amount
        print(f"Withdraw         : {self.balance}")

    @classmethod
    def bank_name(self):
        print("Bank Name         : National Bank of India")

    def minimum_balance(self):
        print("Minimum Balance  : 1000")


b1 = BankAccount(10000000,"Rutvik",50000)
b1.bank_name()
b1.display_account()
b1.deposit(400)
b1.withdraw(900)
b1.minimum_balance()

b2 = BankAccount(10000000,"Rutvik",50000)
b2.bank_name()
b2.display_account()
b2.deposit(400)
b2.withdraw(900)
b2.minimum_balance()

b3 = BankAccount(10000000,"Rutvik",50000)
b3.bank_name()
b3.display_account()
b3.deposit(400)
b3.withdraw(900)
b3.minimum_balance()

b4 = BankAccount(10000000,"Rutvik",50000)
b4.bank_name()
b4.display_account()
b4.deposit(400)
b4.withdraw(900)
b4.minimum_balance()


# Store

# * Account Number
# * Customer Name
# * Balance

# Create the following methods.

# ### Instance Method

# **display_account()**

# Display account details.

# ### Instance Method

# **deposit(amount)**

# Increase the account balance.

# ### Instance Method

# **withdraw(amount)**

# Decrease the account balance.

# ### Class Method

# **bank_name()**

# Display

# ```text
# National Bank of India
# ```

# ### Static Method

# **minimum_balance()**

# Display

# ```text
# Minimum Balance : ₹1000
# ```

# ### Requirements

# * Create **3 customer accounts**.
# * Perform one deposit operation.
# * Perform one withdrawal operation.
# * Display the updated balance.

