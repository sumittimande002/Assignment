# # Question 3: Online Shopping Order System (Intermediate)

# ### Problem Statement

# An e-commerce company wants to generate customer orders.

# Create a class named **Order**.

class Order :
    def __init__(self,Order_ID,Customer_Name,Product_Name,Quantity,Price_Per_Item):
        self.Order_ID = Order_ID
        self.Customer_Name = Customer_Name
        self.Product_Name = Product_Name
        self.Quantity = Quantity
        self.Price_Per_Item = Price_Per_Item

    def display_order(self):
        print("-------------------------------------")
        print("          Order Details   ")
        print("-------------------------------------")
        print(f"Order Id         : {self.Order_ID}")
        print(f"Customer Name    : {self.Customer_Name}")
        print(f"Product Name     : {self.Product_Name}")
        print(f"Quantity         : {self.Quantity}")
        print(f"Price Per Item   : {self.Price_Per_Item}")

    def calculate_total(self):
        total_amount = self.Quantity*self.Price_Per_Item
        print(f"Total Amount     : {total_amount}")

O1 = Order(1001,"Sumit","Oliv Oil",5,500)
O1.display_order()
O1.calculate_total()

O2 = Order(1002,"Kunal","Oliv",5,500)
O2.display_order()
O2.calculate_total()

O3 = Order(1003,"Kavita","Brade",5,50)
O3.display_order()
O3.calculate_total()

O4 = Order(1004,"Rajesh","Gruu ",5,10)
O4.display_order()
O4.calculate_total()

O5 = Order(1005,"Rahul","Parle G",50,100)
O5.display_order()
O5.calculate_total()


# Initialize the following details using a constructor:

# * Order ID
# * Customer Name
# * Product Name
# * Quantity
# * Price Per Item

# Create the following methods:

# * **display_order()**
# * **calculate_total()**

# The total amount should be calculated as:

# ```text
# Total Amount = Quantity × Price Per Item
# ```

# ### Requirements

# * Create **5 Order objects**.
# * Display complete order details.
# * Display the total amount of every order.

# ### Expected Output Format

# ```text
# -----------------------------------------
# Order Details
# -----------------------------------------

# Order ID        : ORD101
# Customer Name   : Priya
# Product Name    : Laptop
# Quantity        : 2
# Price Per Item  : ₹55,000

# Total Amount    : ₹1,10,000
# ```