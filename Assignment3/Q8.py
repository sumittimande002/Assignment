# 8.Write a program to count the frequency of each element in a list using a dictionary.

l = [10,20,30,50,10,32,40,80,90,80,40,20,30]
l.sort()
# print(type(l))
# d = {"Values":(l)}
# print(type(d))
# print(d)
# s = set(d.values())
# print(s)


fraq = {}
for i in l:
    if i in fraq:
        fraq[i]+=1
    else:
        fraq[i] = 1

print("Frequency of element is : ")
for key ,value in fraq.items():
    print(key ," : ",value)