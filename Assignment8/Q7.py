# ### 7. Function Chaining

# **Question:**
# Create two functions: add(a, b) and multiply(a, b).
def add(a,b):
    return (a + b)

def multiply(a , b):
    return a * b
      
# Call multiply using result of add.

print(multiply(add(2,3) ,4))
print(multiply(add(10,5),2))
print(add(10,2))
print(multiply(add(50,2),2))
# **Test Case 1:**
# Input:
# multiply(add(2,3),4)

# Expected Output:
# 20

# **Test Case 2:**
# Input:
# multiply(add(10,5),2)

# Expected Output:
# 30