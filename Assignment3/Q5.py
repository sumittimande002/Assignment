# 5.Create a dictionary with employee details (id, name, salary).
# Perform:
d = {"id" : 101 ,"name" :"Sumit" ,"salary":50000}
print(d,type(d))
# a)Add a new key
d["Address"] = "At Wardha"
print(d)

# b)Update salary
d.update({"salary":60000})
print(d) 

# c)Delete a key
d.pop("salary")
print(d)