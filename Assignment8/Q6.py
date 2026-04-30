# ## SECTION 3: RETURN VS PRINT
# ===========================================================================

# ### 6. Print vs Return (Square)

# **Question:**
# Create:

# * One function that prints square
def square_print(num):
    print(num**2)

square_print(5)

# * One function that returns square
def square_return(num):
    return num**2

res = square_return(5)
print(res)
# **Test Case 1:**

# Input:
# square_print(5)

# Output:
# 25

# Input:
# result = square_return(5)
# print(result * 10)

# Output:
# 250

# **Test Case 2:**
# Input:
# square_print(3)

# Output:
# 9
