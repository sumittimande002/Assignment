# # Question 5: Food Delivery Order System (Advanced)

# ### Problem Statement

# A food delivery application wants to display customer order details.

# Create a class named **FoodOrder**.

class FoodOrder:
    def __init__(self,Order_Id,Customer_Name,Restaurant_Name,Food_Item,Quantity,Price_Per_Item):
        self.Order_Id = Order_Id
        self.Customer_Name = Customer_Name
        self.Restaurant_Name = Restaurant_Name
        self.Food_Item = Food_Item
        self.Quantity = Quantity
        self.Price_Per_Item = Price_Per_Item

    def display_order(self):
        print("-----------------------------------------")
        print("           Food Order Details            ")
        print("-----------------------------------------")
        print(f"Order ID        : {self.Order_Id}")
        print(f"Customer Name   : {self.Customer_Name}")
        print(f"Restaurant Name : {self.Restaurant_Name}")
        print(f"Food Item       : {self.Food_Item}")
        print(f"Quantity        : {self.Quantity}")
        print(f"Price Per Item  : {self.Price_Per_Item}")

        


    def calculate_bill(self):
        total_Bill = self.Quantity * self.Price_Per_Item
        print(f"Total Bill      : {total_Bill}")

f1 = FoodOrder(1001,"Rajesh","Jakii Restaurant","Ice",2,500)
f1.display_order()
f1.calculate_bill()


f2 = FoodOrder(1002,"Sumit","Ankaaa Restaurant","ulaaa",4,50)
f2.display_order()
f2.calculate_bill()


f3 = FoodOrder(1003,"Ram","Rakull Restaurant","Veggs",4,1500)
f3.display_order()
f3.calculate_bill()


f4 = FoodOrder(1004,"Ankush","Akuuu Restaurant","Eggs",6,10)
f4.display_order()
f4.calculate_bill()


f5 = FoodOrder(1005,"Raj","Kluuu Restaurant","Ice disk",5,450)
f5.display_order()
f5.calculate_bill()

# The class should store the following information:

# * Order ID
# * Customer Name
# * Restaurant Name
# * Food Item
# * Quantity
# * Price per Item

# Create the following methods:

# * **display_order()**
# * **calculate_bill()**

# The total bill should be calculated as:

# ```
# Total Bill = Quantity × Price per Item
# ```

# ### Requirements

# * Create **5 FoodOrder objects**.
# * Display the complete order details.
# * Display the calculated total bill for every order.

# ### Expected Output Format

# ```
# ---------------------------------
# Food Order Details
# ---------------------------------

# Order ID        : 1001
# Customer Name   : Sai
# Restaurant      : Paradise
# Food Item       : Chicken Biryani
# Quantity        : 2
# Price per Item  : ₹350
# Total Bill      : ₹700

