# ### 15. Combined Example (map + filter)

# **Question:**
# Given a list of numbers:

# * First filter even numbers
input1 = [1,2,3,4,5,6]
input2 = [10,15,20]
filter_result = list(filter(lambda l : l % 2 == 0 , input2))

# * Then square them using map()
map_square = list(map(lambda l : l **2 , filter_result))

print(map_square)


# **Test Case 1:**
# Input:
# [1,2,3,4,5,6]

# Expected Output:
# [4,16,36]

# **Test Case 2:**
# Input:
# [10,15,20]

# Expected Output:
# [100,400]