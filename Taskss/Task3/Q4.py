# # Question 4: Online Shopping Inventory System (Intermediate)

# ### Problem Statement

# An online shopping company wants to maintain product information.

# Create a class named **Product**.

class Product:
    def __init__(self,Product_Id,Product_Name,Brand,Price):
        self.Product_Id = Product_Id
        self.Product_Name = Product_Name
        self.Brand = Brand
        self.Price = Price

    GST = "18%"

    def display_product(self):
        discount = "10%"
        print("--------------------------------")
        print("        Product Details ")
        print("--------------------------------")
        print(f"Product ID      : {self.Product_Id}")
        print(f"Product Name    : {self.Product_Name}")
        print(f"Brand           : {self.Brand}")
        print(f"Price           : {self.Price}")
        print(f"Discount        : {discount}")
        print(f"GST             : {self.GST}")



p1 = Product(101,"Pepsi","Zuuu",500)
p1.display_product()


p2 = Product(101,"Pepsi","Zuuu",500)
p2.display_product()


p3 = Product(101,"Pepsi","Zuuu",500)
p3.display_product()


p4 = Product(101,"Pepsi","Zuuu",500)
p4.display_product()


p5 = Product(101,"Pepsi","Zuuu",500)
p5.display_product()

# Use:

# ### Instance Variables

# * Product ID
# * Product Name
# * Brand
# * Price

# ### Class Variable

# * GST = 18%

# Create a method named **display_product()**.

# Inside the method, create a **Local Variable**

# ```text
# Discount = 10%
# ```

# Display:

# * Product Details
# * GST
# * Discount

# ### Requirements

# * Create **5 Product objects**.
# * Display the details of all products.

# ### Expected Output Format

# ```text
# -----------------------------------------
# Product Details
# -----------------------------------------

# Product ID      : P101
# Product Name    : Laptop
# Brand           : Dell
# Price           : ₹65,000

# GST             : 18%
# Discount        : 10%
