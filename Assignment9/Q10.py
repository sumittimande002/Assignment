# ## SECTION 5: reduce()

# (Note: Import reduce from functools)

# ---

# ### 10. Find Sum of List Using reduce()

# **Question:**
# Use reduce() to find sum of elements.
from functools import reduce

input1 = [1,2,3,4]
input2 = [5,5,5]

result = reduce(lambda a , b : a + b, input2)
print("Sum of Numbers : ",result)


# **Test Case 1:**
# Input:
# [1,2,3,4]

# Expected Output:
# 10

# **Test Case 2:**
# Input:
# [5,5,5]

# Expected Output:
# 15