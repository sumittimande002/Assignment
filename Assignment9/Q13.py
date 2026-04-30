# ### 13. Filter High Salary Employees

# **Question:**
# Given a list of salaries, filter salaries above 50,000.
input1 = [30000, 60000, 45000, 80000]
input2 = [55000, 40000, 75000]

result = list(filter(lambda l : l > 50000 , input2))
print(result)

# **Test Case 1:**
# Input:
# [30000, 60000, 45000, 80000]

# Expected Output:
# [60000, 80000]

# **Test Case 2:**
# Input:
# [55000, 40000, 75000]

# Expected Output:
# [55000, 75000]