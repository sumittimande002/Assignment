# # Question 3: Online Shopping System (Intermediate)

# ### Problem Statement

# An online shopping company wants to generate customer bills.

# Create a class named **Product**.

class Product:
    def __init__(self, product_id, product_name, quantity, price):
        self.product_id = product_id
        self.product_name = product_name
        self.quantity = quantity
        self.price = price
    
    def display_product(self):
        print(f"Product ID     : {self.product_id}")
        print(f"Product Name   : {self.product_name}")
        print(f"Quantity       : {self.quantity}")
        print(f"Price          : {self.price}")

    def calculate_bill(self):
        total_amount = self.quantity * self.price
        print(f"Total Amount   : {total_amount}")

    @classmethod
    def store_name(cls):
        print("Store Name     : Python Shopping Mart")

    @staticmethod   
    def gst_percentage():
        print("GST            : 18%")


p1 = Product("P101", "Laptop", 2, 60000)
p1.store_name()
p1.display_product()
p1.calculate_bill()
p1.display_product
p1.gst_percentage()
# Store

# * Product ID
# * Product Name
# * Quantity
# * Price

# Create the following methods.

# ### Instance Method

# **display_product()**

# Display all product details.

# ### Instance Method

# **calculate_bill()**

# Calculate

# ```text
# Total Amount = Quantity × Price
# ```

# ### Class Method

# **store_name()**

# Display

# ```text
# Python Shopping Mart
# ```

# ### Static Method

# **gst_percentage()**

# Display

# ```text
# GST : 18%
# ```

# ### Requirements

# * Create **5 Product objects**.
# * Display product information.
# * Display total bill.

# ### Expected Output Format

# ```text
# -----------------------------------------
# Product Details
# -----------------------------------------

# Store Name     : Python Shopping Mart

# Product ID     : P101
# Product Name   : Laptop
# Quantity       : 2
# Price          : ₹60,000

# Total Amount   : ₹1,20,000

# GST            : 18%
# ```
