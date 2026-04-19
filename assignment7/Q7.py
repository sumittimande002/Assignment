"""
7.Write a python program to print a complete diamond shape using stars (*) with nested loops.

    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
"""
row = int (input("Enter a Number : "))
for i in range (1, row+1 ,+1):
    for j in range (row-i):
        print(" ",end="")
    for k in range(1,2*i):
        print("*",end="")
    print()

for i in range (row-1,0,-1):
    for j in range(row - i):
        print(" ",end="")
    for k in range(1,2*i):
        print("*",end="")
    print()
