# # Question 2: Bank Account Security System (Beginner)

# ### Problem Statement

# A bank wants to protect customer account balances from direct access.

# Create a class named **BankAccount**.
class BankAccount:
    def __init__(self, account_number, customer_name, balance):
        self.account_number = account_number
        self.customer_name = customer_name
        self.__balance = balance  

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Withdrawal amount must be positive and less than or equal to the available balance.")
    
    def get_balance(self):
        return self.__balance
    
    def display_customer(self):
        print("-----------------------------------------")
        print("Customer Details")
        print("-----------------------------------------")
        print(f"Customer Name   : {self.customer_name}")
        print(f"Account Number  : {self.account_number}")
        print(f"\nAvailable Balance : {self.__balance:,}")
    

b = BankAccount(123456789, "Sai", 85000)
b.display_customer()
b.display_customer
b.deposit(5000)
b.withdraw(2000)
b.display_customer()
    

# Store the following information:

# * Account Number
# * Customer Name
# * Private Variable: **Balance**

# Create the following methods:

# * **deposit(amount)**
# * **withdraw(amount)**
# * **get_balance()**
# * **display_customer()**

# ### Requirements

# * Create **3 BankAccount objects**.
# * Perform deposit and withdrawal operations using methods only.
# * Balance should never be modified directly.

# ### Expected Output Format

# ```text
# -----------------------------------------
# Customer Details
# -----------------------------------------

# Customer Name   : Sai
# Account Number  : 123456789

# Available Balance : ₹85,000
