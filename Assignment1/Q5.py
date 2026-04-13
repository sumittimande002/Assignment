# 5. Program to Calculate Distance Traveled
# Problem Statement: Write a program to calculate the distance traveled by a vehicle. The program 
# should take the speed of the vehicle and the time it has been traveling as input, and calculate
#  the total distance traveled.

speed =float(input("Enter a Speed of Vehical : "))
time = float(input("Enter a Time : "))
total_distance = speed * time
print("Total Distance Traveled By Vehicle : " ,int(total_distance))