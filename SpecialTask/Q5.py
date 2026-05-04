## 5. Program to Create a Car Information System

# **Problem Statement:**
# Create a `Car` class. The constructor should initialize brand, model, and price. Create a method 
# to display car details and apply a discount (5%).

class Car:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price
    
    def car_details(self):
        print("Brand : ",self.brand)
        print("Model : ",self.model)
        discount = self.price - (self.price*5/100)
        print("Discount Price : ",discount)

c = Car("Toyota","Innova",2000000)
c.car_details()
print("==============")
c1 = Car("Hyundai","i20",800000)
c1.car_details()
print("==============")
c1 = Car("Tata","Nexon",1000000)
c1.car_details()

        