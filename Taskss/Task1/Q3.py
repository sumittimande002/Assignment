# # Question 3: Product Catalog System (Intermediate)

# ### Problem Statement

# An online shopping company wants to display the details of the products available on its website.

# Create a class named **Product**.

class Product:
    def __init__(self,Product_ID,Product_Name,Brand,Price):
        self.Product_ID = Product_ID
        self.Product_Name = Product_Name
        self.Brand = Brand
        self.Price = Price

    def display_product(self):
        print("------------------------------")
        print("Product details")
        print("------------------------------")
        print(f"Product Id   : {self.Product_ID}")
        print(f"Product Name : {self.Product_ID}")
        print(f"Brand        : {self.Brand}")
        print(f"Price        : {self.Price}")


Laptop = Product(101,"Laptop","NA",50000)
Laptop.display_product()
Mobile = Product(102,"Mobile","IQ Z10",60000)
Mobile.display_product()
Keyboard = Product(103,"Keyboard","Livi",4000)
Keyboard.display_product()
Mouse = Product(104,"Mouse","Lenevo",3000)
Mouse.display_product()
Monitor = Product(105,"Monitor","Redmi",2000)
Monitor.display_product()
print("Total Product Created 5.")


# The class should store the following information:

# * Product ID
# * Product Name
# * Brand
# * Price

# Create a method named **display_product()** to display the product details.

# ### Requirements

# Create objects for the following products:

# * Laptop
# * Mobile
# * Keyboard
# * Mouse
# * Monitor

# Display the details of all products.

# ### Bonus Task

# After displaying all the products, print:

# ```
# Total Products Created : 5
# ```

# *(Do not use class variables for this assignment.)*

