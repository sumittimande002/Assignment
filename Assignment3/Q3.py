# 3.Create a tuple with mixed data types and:
t = (10,20,"Rahul",90,"R","Kunal")

# a)Access elements using indexing
print(type(t))

print(t[5])
print(t[2])

# b)Explain why tuples are immutable
#t[1] = 5000 # it not support assignment

# c)Convert a tuple into a list, modify an element, and convert it back into a tuple.
l = list(t)
print(type(l))
t1 =tuple(l)
print(type(t1))