# 8.Write a program to check whether a given number is a prime number using loops.

n = int(input("Enter a Number : "))
if n <=1 :
    print("Not Prime")
else :
    for i in range(2, n):
        if n % i == 0 :
         print("Not Prime ")
         break
    else:
        print("Number is Prime")