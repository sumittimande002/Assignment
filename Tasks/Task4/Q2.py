
## 32. Program to Count Vowels in a String

# **Problem Statement:** Write a program to count the number of vowels in a 
# given string.
count = 0
str = input("Enter string : ")
vovel = "aeiouAEIOU"
for i in str:
    if( i in vovel):
        count+=1

print(count)