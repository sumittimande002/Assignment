"""3.Create a tuple with mixed data types and:

    a)Access elements using indexing

    b)Explain why tuples are immutable

    c)Convert a tuple into a list, modify an element, and convert it back into a tuple.
"""

t = (10,20,"Rahul",90,"R","Kunal")
print(type(t))
print(t[5])
print(t[2])

# cls
#t[1] = 5000 # it not support assignment
print(t)