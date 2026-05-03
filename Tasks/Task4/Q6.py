## 36. Program to Remove Duplicates from a List

# **Problem Statement:** Write a program to remove duplicate elements from a list.

l = [10,20,50,10,80,40,80]
print(l)
t = set(l)
print(t)

uniq = []
for i in l:
    if(i not in uniq):
        uniq.append(i)

print(uniq)