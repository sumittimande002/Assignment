## 6. Program to Find Largest of Three Numbers

# **Problem Statement:** Write a program to find the largest among three numbers.

a = int(input("Value for A : "))
b = int(input("Value for B : "))
c = int(input("Value for C : "))
if(a>b and a>c):
    print("A is Largest number : " ,a)
elif(b>a and b >c):
    print("B is Largest Number : ", b)
elif(c>a and c>b):
    print("C is Largest Number : ", c)
else:
    print("a, b , c are same",a,b,c)