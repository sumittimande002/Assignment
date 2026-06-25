# # Question 4: Vehicle Rental System (Intermediate)

# ### Problem Statement

# A vehicle rental company wants to calculate rental charges for different vehicle types.

# Create an **Abstract Class** named **Vehicle**.

# Create the following abstract methods:

# * rental_price()
# * fuel_type()
# * vehicle_details()

from abc import ABC ,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def rental_price():
        pass

    @abstractmethod
    def fuel_type():
        pass

    @abstractmethod
    def vehicle_details():
        pass


class Bike(Vehicle):
    def vehicle_details(self):
        print("----------------------")
        print("   Vehical Details   ")
        print("----------------------")
        print("Vehical Type : Bike")

    def fuel_type(self,type):
        print(f"Fuel Type    : {type}")

    def rental_price(self,price):
        print(f"Rental Price : {price}")

class Car(Vehicle):
    
    def vehicle_details(self):   
        print("----------------------")
        print("   Vehical Details   ")
        print("----------------------")
        print("Vehical Type : Car")

    def fuel_type(self,type):
        print(f"Fuel Type    : {type}")

    def rental_price(self,price):
        print(f"Rental Price : {price}")
    

class Bus(Vehicle):
    def vehicle_details(self):  
        print("----------------------")
        print("   Vehical Details   ")
        print("----------------------")
        print("Vehical Type : Bus")

    def fuel_type(self,type):
        print(f"Fuel Type    : {type}")

    def rental_price(self,price):
        print(f"Rental Price : {price}")

b = Bike()
c = Car()
b1 = Bike()
b.vehicle_details()
b.fuel_type("Petrol")
b.rental_price(2500)

c.vehicle_details()
c.fuel_type("Petrol")
c.rental_price(8500)

b1.vehicle_details()
b1.fuel_type("Petrol")
b1.rental_price(500)

# Create the following child classes:

# * Bike
# * Car
# * Bus

# Each vehicle type should implement the methods according to its rental policy.

# ### Requirements

# * Create one object for each vehicle.
# * Display rental charges.
# * Display fuel type.
# * Display vehicle details.

# ### Expected Output Format

# ```text
# -----------------------------------------
# Vehicle Details
# -----------------------------------------

# Vehicle Type      : Car

# Fuel Type         : Petrol

# Rental Price      : ₹2,500 / Day
