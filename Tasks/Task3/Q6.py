
## 26. Program to Check Prime Number

# **Problem Statement:** Write a program to check whether a given number is prime.
# if (number == 0 or number == 1):
#     print("Number is Prime")
# else:
# if (number == 2):
#     print("Prime Number")
# else :
#     if(number % 2 == 0 ):
#         print("Not Prime")
#     else:
#         print("Prime Number")
number = int(input("Enter a Number : "))


if (number <= 1 ):
    print("Not Prime")
else:
    for i in range(2,number):
        if(number % i == 0):
            print("Not Prime.")
            break
    else:
        print("Prime Number")