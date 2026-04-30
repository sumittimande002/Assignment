# ## SECTION 4: LOGICAL THINKING WITH FUNCTIONS
# ===================================================================

# ### 8. Even & Odd Counter

# **Question:**
# Write a function that returns count of even and odd numbers.

def even_odd(val):
    even_count = 0
    odd_count = 0
    for i in val:
        if i % 2 == 0:
            even_count += 1
        else :
            odd_count += 1

    print("Even no :",even_count)        
    print("Odd No : ", odd_count)

    
even_odd([1,2,3,4,5])

# **Test Case 1:**
# Input:
# [1,2,3,4,5]

# Expected Output:
# Even count: 2
# Odd count: 3

# **Test Case 2:**
# Input:
# [2,4,6]

# Expected Output:
# Even count: 3
# Odd count: 0