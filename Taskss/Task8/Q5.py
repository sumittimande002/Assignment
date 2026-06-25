
# # Question 5: Food Delivery System (Method Overriding + Duck Typing)

# ### Problem Statement

# A food delivery application supports multiple restaurant partners.

# Create the following classes:

# * Dominos
# * KFC
# * Paradise

class Dominos:
    def order_food(self,order,status):
       print("----------------------")
       print("  Restaurent Details ")
       print("----------------------")
       print("Restaurant  : Dominos")
       print(f"Food Order : {order}")
       print(f"Status     : {status}")



class KFC:
    def order_food(self,order,status):
        print("----------------------")
        print("Restaurant  : KFC")
        print(f"Food Order : {order}")
        print(f"Status     : {status}")
      

class Paradise:
    def order_food(self,order,status):
        print("----------------------")
        print("Restaurant  : Paradise")
        print(f"Food Order : {order}")
        print(f"Status     : {status}")
      

def place_order(restaurant,order,status):
    restaurant.order_food(order,status)

place_order(Dominos(),"Veg Pizza","Order Confirmed")
place_order(KFC(),"Veg Pizza","Order Confirmed")
place_order(Paradise(),"Veg Pizza","Order Confirmed")



# Each class should contain the method:

# * order_food()

# Create a function named:

# * place_order(restaurant)

# The function should call **order_food()** without checking the object type.

# ### Requirements

# * Demonstrate **Method Overriding** and **Duck Typing**.
# * Display restaurant-specific order details.

# ### Expected Output Format

# ```text
# -----------------------------------------
# Food Order Details
# -----------------------------------------

# Restaurant      : Dominos
# Food Ordered    : Veg Pizza
# Status          : Order Confirmed

# -----------------------------------------

# Restaurant      : KFC
# Food Ordered    : Chicken Bucket
# Status          : Order Confirmed

# -----------------------------------------

# Restaurant      : Paradise
# Food Ordered    : Chicken Biryani
# Status          : Order Confirmed
# ```
