# 7.Declare two sets, perform and display: Union, Intersection, Difference.
s1 = {10,50,40,30,60}
s2 = {20,40,80,90,77}
print(type(s1),type(s2))
# Union
print(s1.union(s2))

#Intersection
print(s1.intersection(s2))

# Difference
print(s1.difference(s2))
print(s2.difference(s1))