# ### 5. Multiple Exception Handling

# **Question:**
# Write a program that:
try:
    l = [10, 20, 30]
    a = int(input("Enter a index Number : "))
    print(l[a])
except IndexError:
    print("Error: Index out of range.")
except ValueError:
    print("Error: Invalid index input.")


# * Takes index input from user
# * Prints element from list
# * Handles IndexError and ValueError

# **Test Case 1:**
# List: [10, 20, 30]
# Input: 1

# Output:
# Element: 20

# **Test Case 2:**
# Input: 5

# Output:
# Error: Index out of range.

# **Test Case 3:**
# Input: abc

# Output:
# Error: Invalid index input.

