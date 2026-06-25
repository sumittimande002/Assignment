# # Question 1: Online Payment System (Method Overriding)

# ### Problem Statement

# An e-commerce application supports multiple payment methods.

# Create a **Parent Class** named **Payment** with a method:

# * make_payment()


class Payment:
    def make_payment(self):
        pass


class CreditCardPayment(Payment):
    def make_payment(self,amount,status):
        print("------------------------------------")
        print("          Payment Details    ")  
        print("------------------------------------")
        print(f"Type     :  Credit Card Payment")
        print(f"Amount   : {amount}")
        print(f"Status   : {status}")
        print("------------------------------------")

class DebitCardPayment(Payment):
     def make_payment(self,amount,status):
        print(f"Type     :  Debit Card Payment")
        print(f"Amount   : {amount}")
        print(f"Status   : {status}")
        print("-------------------------------------")

class UpiPayment(Payment):
     def make_payment(self,amount,status):
        print(f"Type     :  UPI Payment")
        print(f"Amount   : {amount}")
        print(f"Status   : {status}")


cc = CreditCardPayment()
cc.make_payment("2,500","Payment Successful")
dd = DebitCardPayment()
dd.make_payment("1,500","Payment Successful")
up = UpiPayment()
up.make_payment("850","Payment Successful")

# Create the following child classes:

# * CreditCardPayment
# * DebitCardPayment
# * UpiPayment

# Each child class should override the **make_payment()** method and display its own payment process.

# ### Requirements

# * Create one object for each payment type.
# * Call the same method using different objects.
# * Observe different outputs using polymorphism.

# ### Expected Output Format

# ```text
# -----------------------------------------
# Payment Details
# -----------------------------------------

# Payment Method : Credit Card
# Amount         : ₹2,500
# Status         : Payment Successful

# -----------------------------------------

# Payment Method : UPI
# Amount         : ₹850
# Status         : Payment Successful
# ```
