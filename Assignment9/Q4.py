# 4. Function as Argument

# **Question:**
# Create a function apply_operation(func, a, b)
# It should take a function and two numbers.
def add (a ,b):
    return a+b

def sub(a , b):
    return a - b

def apply_operation (func ,a , b):
    return func( a , b)
result = apply_operation(add,5,2)
print(result)

sub_res = apply_operation(sub ,50,6)
print(sub_res)

