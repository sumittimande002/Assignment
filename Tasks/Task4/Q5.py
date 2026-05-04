
## 35. Program to Find Maximum Element in a List

# **Problem Statement:** Write a program to find the maximum element in a list.

l = [1,2,3,5,70,2]
print(max(l))

# l.sort()
# print(l[-1])

value = l[1]
for i in l:
    if value < i:
        max_value = i

print(max_value)

# for min value
# for i in l :
#     if value > i:
#         min_value = i
# print(min_value)

