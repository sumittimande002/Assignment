# 1. Program to Calculate the Area of a Circle
# Problem Statement: Write a program to calculate the area of a circle.
# The program should take the radius as input and calculate the
# area of the circle. Use the appropriate constant for (\pi) to 
# perform the calculation.

Pi = 3.14159
radius = float(input("Enter a radius : "))
Area = Pi *radius**2
print("Area of the circle : " ,Area)