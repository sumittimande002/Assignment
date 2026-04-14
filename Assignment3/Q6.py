# 6.Write a program to iterate through a dictionary and print: Keys, Values ,
# Key-value pairs.
d = {"id" : 101 ,"name" :"Sumit" ,"salary":50000}

# Keys
for keys in d:
    print(keys)

# Values
for values in d.values():
    print(values)
# Key - Values Pair
for keyval in d.items():
    print(keyval)