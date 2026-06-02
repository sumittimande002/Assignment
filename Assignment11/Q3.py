# ### 3. Number Validation Program

# **Question:**
# Take input from user and:

# * Convert to integer
# * Print square of number
try :
    a = int(input("Enter a Number : "))
    print("Squareof No : ",a**2)
except:
    print("Invalid input.")
finally:
    print("Execution completed.")



# Use:

# * try
# * except
# * else
# * finally

# **Test Case 1:**
# Input: 5

# Expected Output:
# Square: 25
# Execution completed.

# **Test Case 2:**
# Input: abc

# Expected Output:
# Invalid input.
# Execution completed.

