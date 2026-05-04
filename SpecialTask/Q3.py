## 3. Program to Build a Product Billing System

# **Problem Statement:**
# Create a `Product` class where the constructor takes product name, price, and quantity.
# Create a method to calculate total cost and display bill details.


class Product :
    def __init__(self,name,price,quantity):
        self.name= name
        self.price = price
        self.quantity = quantity
    total = 0
    def total_cost(self):
        total = self.price*self.quantity
        print("Total : ",total)

    def bill(self):
        print("Name : ",self.name)
        
    
p = Product("Laptop",50000,1)
p.bill()
p.total_cost()
print("======================")
p2 = Product("Mobile",20000,2)
p2.bill()
p2.total_cost()
print("======================")
p3 = Product("Pen",10,5)
p3.bill()
p3.total_cost()
