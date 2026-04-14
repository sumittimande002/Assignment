# 9.Explain the difference between list, tuple, set, and dictionary with 
# one real-time example each
print("---------- List -----------")
l = [10,20,40,50,20,"Sumit"]
print(type(l)) #Type
l.append("Raju")
l.pop(0)
print(l)

print("---------- Tuple -----------")
t = (10,20,40,50,20,"Sumit")
print(type(t))#Type
# t[0]=1000
print(t.index(20))
print(t)

print("---------- Set -----------")
s = {20,40,50,10,20,"Sumit"}
print(type(s))#Type
s.add(500)
s.pop()
print(s)
print()

print("---------- Dictionary -----------")
d = {"Name":"Sumit","Class": 10,"Address":"Wardha"}
print(type(d))#Type
d.pop("Name")
print(d)
print()
