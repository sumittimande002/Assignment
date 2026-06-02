# ### 2. Division Calculator with Exception Handling

# **Question:**
# Write a program that:

# * Takes two numbers from user
# * Performs division
# * Handles ZeroDivisionError and ValueError

try:
    
    a = int(input("Enter a Number : "))
    b = int(input("Enter a Number : "))
    c = a / b
except ZeroDivisionError as zde:
    print("Cannot divide by zero.")
except ValueError as ve:
    print("Invalid input. Please enter numbers only.")




# **Test Case 1:**
# Input:
# 10
# 2

# Expected Output:
# Result: 5.0

# **Test Case 2:**
# Input:
# 10
# 0

# Expected Output:
# Error: Cannot divide by zero.

# **Test Case 3:**
# Input:
# 10
# abc

# Expected Output:
# Error: Invalid input. Please enter numbers only.
