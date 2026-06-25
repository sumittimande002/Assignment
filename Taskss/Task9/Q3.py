# # Question 3: Bank Account System (Private Members)

# ### Problem Statement

# A bank wants to secure customer account information.

# Create a class named **BankAccount**.

# Create the following **Private Attributes**:

# * __account_number
# * __account_holder
# * __balance

class BankAccount:
    def __init__(self,account_number,account_holder,balance):
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = balance 

    def display_account_details(self):
        print(f"Account Number : {self.__account_number}")
        print(f"Account Holder : {self.__account_holder}")
        print(f"Balance        : {self.__balance}")

b = BankAccount(1028532564,"Rakesh",80000)
b.display_account_details()

# print(b.__account_holder())

# Create private methods if necessary.

# Create a public method:

# * display_account_details()

# to display the account information safely.

# ### Requirements

# * Attempt to access private members outside the class.
# * Observe the error.
# * Access them correctly using a public method.

# ### Expected Output Format

# ```text
# -----------------------------------------
# Bank Account Details
# -----------------------------------------

# Account Holder    : Ravi Kumar
# Account Number    : 1234567890
# Balance           : ₹1,25,000
# ```

