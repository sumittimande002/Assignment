## 16. Program to Identify Vowel or Consonant

# **Problem Statement:** Write a program to check whether a character 
# is a vowel or consonant.

a = input("Enter a input : ")
l1 = ["a","e","i","o","u"] 
l2 = ["A","E","I","O","U"]

if(a in l1 or a in l2):
    print("Vowel")
else:
    print("Consonant")