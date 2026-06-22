# # Question 1: Online Payment Gateway System (Basic)

# ### Problem Statement

# An e-commerce company wants to support multiple payment methods using a common interface.

# Create an **Abstract Class** named **Payment**.
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def make_payment(self):
        pass

    @abstractmethod
    def payment_status(self):
        pass

class CreaditCardPayment(Payment):
    def make_payment(self,amount):
        print("--------------------------")
        print( " Payment Details")
        print("--------------------------")
        print("Cridit Card Payment.")
        print(f"Paid Amount : {amount}")

    def payment_status(self):
        print("Credit Card Payment Successful.")

class DebitCardPayment(Payment):
    def make_payment(self,amount):
        print("---------------------------")
        print("Debit Card Payment.")
        print(f"Paid Amount : {amount}")
    def payment_status(self):
        print("Debit Card Payment Successful.")
    

class UpiPayment(Payment):

    def make_payment(self,amount):
        print("---------------------------")
        print("Upi Payment. ")
        print("Paid Amount :",amount)
    
    def payment_status(self):
        print("Upi Payment Successful.")


c = CreaditCardPayment()
c.make_payment(400)
c.payment_status()


d = DebitCardPayment()
d.make_payment(5000)
d.payment_status()

u = UpiPayment()
u.make_payment(7000)
u.payment_status()

# Create the following abstract methods:

# * **make_payment()**
# * **payment_status()**

# Create the following child classes:

# * CreditCardPayment
# * DebitCardPayment
# * UpiPayment

# Each class should implement the abstract methods differently.

# ### Requirements

# * Create one object for each payment method.
# * Display the payment process and payment status.

# ### Expected Output Format

# ```text
# -----------------------------------------
# Payment Details
# -----------------------------------------

# Payment Method : Credit Card
# Amount Paid    : ₹2,500
# Status         : Payment Successful

# -----------------------------------------

# Payment Method : UPI
# Amount Paid    : ₹1,200
# Status         : Payment Successful
# ```
