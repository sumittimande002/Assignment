# # Question 3: Vehicle Information System (Duck Typing)

# ### Problem Statement

# A transport company manages different types of vehicles.

# Create the following classes:

# * Car
# * Bike
# * Bus

class Car:
    def vehicle_info(self):
        print("--------------------")
        print("Vehicle Information")
        print("--------------------")
        print("Type : Car")
        print("Brand : Hyundai")
        print("Fuel : Petrol")

class Bike:
    def vehicle_info(self):
        print("--------------------")
        print("Type : Bike")
        print("Brand : Honda")
        print("Fuel : Petrol")  

class Bus:
    def vehicle_info(self):
        print("--------------------")
        print("Type : Bus")
        print("Brand : Volvo")
        print("Fuel : Diesel")


def display_vehicle(vehicle):
    vehicle.vehicle_info()

display_vehicle(Bike())
display_vehicle(Car())
display_vehicle(Bus())
# Each class should contain the same method:

# * vehicle_info()

# Create a function named:

# * display_vehicle(vehicle)

# The function should call **vehicle_info()** without checking the object type.

# ### Requirements

# * Demonstrate **Duck Typing**.
# * Pass different objects to the same function.

# ### Expected Output Format

# ```text
# -----------------------------------------
# Vehicle Information
# -----------------------------------------

# Vehicle Type   : Car
# Brand          : Hyundai
# Fuel           : Petrol

# -----------------------------------------

# Vehicle Type   : Bike
# Brand          : Honda
# Fuel           : Petrol

# -----------------------------------------

# Vehicle Type   : Bus
# Brand          : Volvo
# Fuel           : Diesel
# ```
