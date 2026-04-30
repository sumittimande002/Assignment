
# ### 11. Find Product of List Using reduce()

# **Question:**
# Use reduce() to find product of elements.
from functools import reduce

input1 = [1,2,3,4]
input2 = [2,3,5]

result = reduce(lambda a , b:a* b ,input2)
print(result)

# **Test Case 1:**
# Input:
# [1,2,3,4]

# Expected Output:
# 24

# **Test Case 2:**
# Input:
# [2,3,5]

# Expected Output:
# 30
