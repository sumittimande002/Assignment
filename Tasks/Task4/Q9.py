## 39. Program to Check Prime Number using Function

# **Problem Statement:** Write a function to check whether a number is prime.
num = int(input("Enter a Number : "))
 
def prime(num):
    # num = int(input("Enter a Number : "))
    if num <= 1 :
        prime("True")
    else:
        for i in range(2,num):
            if(num % i == 0):
                print("False")
                break
        else:
            print("True")

prime(num)