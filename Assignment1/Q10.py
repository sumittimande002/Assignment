# 10. Splitting into the Teams
# Problem Statement: Write a program to divide a group of people into teams of two. 
# The program should take the number of people as input and output the number of 
# teams that can be formed and how many people will be left without a team.

Num_People = int(input("Enter a Number of People : "))
cls = int(Num_People/2)
res = Num_People % 2
print("Number of Teams : " , cls)
print("Leftover People : ", res)