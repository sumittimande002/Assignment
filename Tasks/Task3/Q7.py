## 27. Program to Print Prime Numbers in a Range

# **Problem Statement:** Write a program to print all prime numbers 
# between two given numbers.

s_number = int(input("Enter Number : "))
l_number = int(input("Emnter Number : "))
prime = []
for i in range (s_number , l_number + 1):
    if i > 1 :
        for j in range(2 , i):
            if (i % j == 0 ):
             break
        else:
            prime.append(i)


print(prime)
    
