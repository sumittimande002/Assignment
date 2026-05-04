## 2. Program to Design a Bank Account System

# **Problem Statement:**
# Create a `BankAccount` class where the constructor initializes account holder name and balance.
# Implement methods to deposit, withdraw, and display balance.

class BankAccount:
    def __init__(self,name,balance):
        self.name =name
        self.balance = balance

    def deposit(self ,amount):
        self.balance += amount
        print("Name : ",self.name)
        print("Your Current Balance is : ",self.balance)
    
    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance-=amount
            print("Name : ",self.name)
            print("Your Current Balance : ",self.balance)
        else:
            print("Name : ",self.name)
            print("Balance is Low",self.balance)
    # def display_info(self ):
    #     print("Your Name : ",self.name)
    #     print("Your Current Balance : ",self.balance)
        

b = BankAccount("Sumit",1000)
b.withdraw(500)
# b.display_info()
print("==========================")
b1 = BankAccount("Akash",1000)
b1.withdraw(1500)
# b1.deposit(1000)
# b1.display_info()
print("==========================")
b3 = BankAccount("Rohit",500)
b3.deposit(200)


