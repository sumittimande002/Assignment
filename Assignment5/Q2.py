# 2.Write a program to count the number of vowels in a given string using string methods.

count = 0

ch = input("Enter a String : ")
for i in ch:
    if ( i in "aeiouAEIOU"):
        count+=1
print("Count of Vowels : ",count)
print("---------------------------------")

l = ["a","e","i","o","u","A","E","I","O","U"]
count1 = 0
for i in ch:
    if i in l:
        count1+=1
print("Count of Vowels : ",count1)
