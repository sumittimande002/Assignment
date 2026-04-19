"""
5.Write a program to generate the multiplication table of a given number up to 10.
expected output : 
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
.
.
.
5 * 10 = 50"""

n = int(input("Enter a Number : "))

for i in range(1,11):
    print(f"{ n } * { i } = {n*i}")