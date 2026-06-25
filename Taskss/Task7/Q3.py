
# # Question 3: Vehicle Showroom (Hierarchical Inheritance)

# ### Problem Statement

# A vehicle showroom sells different types of vehicles.

# Create a **Parent Class** named **Vehicle**.

# Attributes:

# * Brand
# * Model
# * Price

class Vehicle:
    def __init__(self, Brand, Model, Price):
        self.Brand = Brand
        self.Model = Model
        self.Price = Price

    def vehicle_details(self):
        print("---------------------------------")
        print("      Vehical Details")
        print("----------------------------------")
        print(f"Brand             : {self.Brand}")
        print(f"Model             : {self.Model}")
        print(f"Price             : {self.Price}")



# Method:

# * vehicle_details()

# Create the following child classes:

# * Car
# * Bike
# * Truck

class Car(Vehicle):
    def __init__(self, Brand, Model, Price,Doors):
        super().__init__(Brand, Model, Price)
        self.Doors = Doors


    def display_car(self):
        self.vehicle_details()
        print(f"Vehicle Type      : Car")
        print(f"Doors             : {self.Doors}")

c = Car("Hyundai","Creta",520000,4)
c.display_car()
        
        

        

class Bike(Vehicle):
    def __init__(self, Brand, Model, Price,Engine_Capacity):
        super().__init__(Brand, Model, Price)
        self.Engine_Capacity = Engine_Capacity

    def display_bike(self):
        self.vehicle_details()
        print(f"Vehical Type      : Bike")
        print(f"Engine Capacity   : {self.Engine_Capacity}")
    
b = Bike("Hero","Java",800000,450)
b.display_bike()

class Truck(Vehicle):
    def __init__(self, Brand, Model, Price,Load_Capacity):
        super().__init__(Brand, Model, Price)
        self.Load_Capacity = Load_Capacity
    def display_truck(self):
        self.vehicle_details()
        print("Vehical Type      : Truck")
        print(f"Load Capacity     : {self.Load_Capacity}")


t = Truck("Tata","Icer",78000000,80)
t.display_truck()

# Each child class should contain additional attributes related to that vehicle.

# Example:

# Car

# * Number of Doors

# Bike

# * Engine Capacity

# Truck

# * Load Capacity

# ### Requirements

# * Display details of each vehicle.
# * Demonstrate **Hierarchical Inheritance**.

# ### Expected Output Format

# ```text
# -----------------------------------------
# Vehicle Details
# -----------------------------------------

# Vehicle Type      : Car
# Brand             : Hyundai
# Model             : Creta
# Price             : ₹16,00,000
# Doors             : 5

# -----------------------------------------

# Vehicle Type      : Bike
# Brand             : Royal Enfield
# Model             : Classic 350
# Price             : ₹2,20,000
# Engine Capacity   : 349 CC
# ```
