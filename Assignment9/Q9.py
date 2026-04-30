# ### 9. Filter Students with Passing Marks

# **Question:**
# Given a list of marks, filter students who scored 50 or above.
input1 = [45, 67, 80, 30, 55]
input2 = [90, 40, 49, 75]

result = list(filter(lambda l : l >= 50 , input2))

print(result)
# **Test Case 1:**
# Input:
# [45, 67, 80, 30, 55]

# Expected Output:
# [67, 80, 55]

# **Test Case 2:**
# Input:
# [90, 40, 49, 75]

# Expected Output:
# [90, 75]