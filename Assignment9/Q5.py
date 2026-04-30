# ### 5. Returning a Function

# **Question:**
# Create a function multiplier(n) that returns a function to multiply any
#  number by n.
def double (n):
    return(n *2)

def triple (n):
    return (n * 3)

def multiplier(func , n):
    return func(n)

double_res = (multiplier(double , 5))
print(double_res)
print(multiplier(triple , 4))
