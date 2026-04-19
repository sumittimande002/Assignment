# 4.Write a program to display the multiplication table of a given number using a for loop.

n = int(input("Enter a Number :"))

for i in range(1 , 11):
    print(f" { n } * { i } : {i*n}")