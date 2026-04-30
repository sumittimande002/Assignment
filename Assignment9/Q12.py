# ## SECTION 6: PRACTICAL REAL-TIME EXAMPLES

# ---

# ### 12. Apply 10% Discount Using map()

# **Question:**
# Given a list of prices, apply 10% discount to each price.
input1 = [100, 200, 300]
input2 = [500, 1000]

result = list(map(lambda l : l - (10/100) *l ,input2 ))
print(result)

# **Test Case 1:**
# Input:
# [100, 200, 300]

# Expected Output:
# [90.0, 180.0, 270.0]

# **Test Case 2:**
# Input:
# [500, 1000]

# Expected Output:
# [450.0, 900.0]
