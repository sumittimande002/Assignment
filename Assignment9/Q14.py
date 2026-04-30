# ### 14. Calculate Total Bill Using reduce()

# **Question:**
# Given a list of item prices in cart, calculate total bill.
from functools import reduce
input1 = [250, 150, 100]
input2 = [999, 1]

result = reduce(lambda a , b : a + b , input2)
print(result)


# **Test Case 1:**
# Input:
# [250, 150, 100]

# Expected Output:
# 500

# **Test Case 2:**
# Input:
# [999, 1]

# Expected Output:
# 1000
