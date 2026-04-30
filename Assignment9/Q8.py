# ### 8. Filter Even Numbers

# **Question:**
# Use filter() to extract even numbers from a list.
input1 =  [1,2,3,4,5,6]
input2 =  [10,15,20,25]
result = list(filter (lambda l : l % 2 ==0 ,input2))
print(result)

# **Test Case 1:**
# Input:
# [1,2,3,4,5,6]

# Expected Output:
# [2,4,6]

# **Test Case 2:**
# Input:
# [10,15,20,25]

# Expected Output:
# [10,20]
