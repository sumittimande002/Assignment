# # Question 4: Online Shopping Wallet System (Intermediate)

# ### Problem Statement

# An online shopping company wants to secure customer wallet balances.

# Create a class named **CustomerWallet**.

# Store:

class CustomerWallet:
    def __init__(self, customer_id, customer_name, wallet_balance):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.__wallet_balance = wallet_balance

    def add_money(self,amount):
        self.__wallet_balance += amount

    def purchase(self,amount):
        self.__wallet_balance -= amount

    def check_balance(self):
        print(f"Wallet Balance  : {self.__wallet_balance}")

    def display_customer(self):
        print("---------------------------------------")
        print("        Wallet Balance ")
        print("----------------------------------------")
        print(f"Customer Id     : {self.customer_id}")
        print(f"Customer Name   : {self.customer_name}\n")
        


c1 = CustomerWallet(101,"Rakesh",50000)
c1.add_money(500)
c1.purchase(800)
c1.display_customer()
c1.check_balance()


c2 = CustomerWallet(101,"Rakesh",50000)
c2.add_money(500)
c2.purchase(800)
c2.display_customer()
c2.check_balance()


c3 = CustomerWallet(101,"Rakesh",50000)
c3.add_money(500)
c3.purchase(800)
c3.display_customer()
c3.check_balance()


c4 = CustomerWallet(101,"Rakesh",50000)
c4.add_money(500)
c4.purchase(800)
c4.display_customer()
c4.check_balance()

# * Customer ID
# * Customer Name
# * Private Variable: **Wallet Balance**

# Create the following methods:

# * **add_money(amount)**
# * **purchase(amount)**
# * **check_balance()**
# * **display_customer()**

# Validation Rules

# * Purchase amount should not exceed wallet balance.
# * Negative amounts should not be accepted.

# ### Requirements

# * Create **5 CustomerWallet objects**.
# * Perform wallet recharge.
# * Perform purchase.
# * Display the remaining balance.

# ### Expected Output Format

# ```text
# -----------------------------------------
# Wallet Details
# -----------------------------------------

# Customer ID      : C101
# Customer Name    : Rahul

# Wallet Balance   : ₹4,850
