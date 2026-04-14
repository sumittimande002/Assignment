# 10.Explain operator precedence in Python and write a program showing how 
# precedence affects the result.
a = int(input("Enter a Number : "))
b = int(input("Enter a Number : "))
resu = a+b
print(resu)
resu1 = a+b-(a-b)
print(resu1)
resu2 = (a*b)-b
print(resu2)
resu3 = b - (a*b)
print(resu3)