# Question 3: Food Delivery Application (Intermediate)

# ### Problem Statement

# A food delivery company wants to support multiple restaurant partners.

# Create an **Abstract Class** named **Restaurant**.

# Create the following abstract methods:

# * prepare_food()
# * delivery_time()
# * restaurant_details()
from abc import ABC ,abstractmethod
class Restaurant(ABC):
    @abstractmethod
    def prepare_time():
        pass

    @abstractmethod
    def delivery_time():
        pass

    @abstractmethod
    def restaurant_details():
        pass

class Dominos(Restaurant):
    def restaurant_details(self,food):
        print("--------------------------")
        print("    Restaurant Details  ")
        print("--------------------------")
        print("  Dominos Restaurant  ")
        print(f"Food          : {food}")
    
    def prepare_time(self,time):
        print(f"Prepare Time  : {time} Min")

    def delivery_time(self,time):
        print(f"Delivery Time : {time} Min")

class KFC(Restaurant):
        def restaurant_details(self,food):
            print("--------------------------")
            print("    Restaurant Details  ")
            print("--------------------------")
            print("   KFC Restaurant  ")
            print(f"Food          : {food}")
    
        def prepare_time(self,time):
            print(f"Prepare Time  : {time} Min")

        def delivery_time(self,time):
            print(f"Delivery Time : {time} Min")



class Paradise(Restaurant):
    def restaurant_details(self,food):
        print("--------------------------")
        print("   Restaurant Details  ")
        print("--------------------------")
        print("    Paradise Restaurant  ")
        print(f"Food          : {food}")
    
    def prepare_time(self,time):
        print(f"Prepare Time  : {time} Min")

    def delivery_time(self,time):
        print(f"Delivery Time : {time} Min")


d = Dominos()
k = KFC()
p = Paradise()
d.restaurant_details("Chikan")
d.prepare_time(50)
d.delivery_time(20)

k.restaurant_details("Chikan")
k.prepare_time(50)
k.delivery_time(20)

p.restaurant_details("Chikan")
p.prepare_time(50)
p.delivery_time(20)
# Create the following child classes:

# * Dominos
# * KFC
# * Paradise

# Each restaurant should implement the methods differently.

# ### Requirements

# * Create one object for each restaurant.
# * Display restaurant details.
# * Display food preparation time.
# * Display estimated delivery time.

# ### Expected Output Format

# ```text
# -----------------------------------------
# Restaurant Details
# -----------------------------------------

# Restaurant Name     : Paradise

# Food                : Chicken Biryani

# Preparation Time    : 20 Minutes

# Delivery Time       : 35 Minutes
# ```