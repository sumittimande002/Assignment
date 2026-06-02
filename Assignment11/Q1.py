# ### 1. Identify Error Type

# **Question:**
# Write a program that intentionally produces:

# * A Syntax Error

# if True
#     print("Syntax Errer")



# * A ZeroDivisionError
a = 10
b = 0
try:
    a/b
except ZeroDivisionError as es:
    print(es)
"""
# * A NameError
try:
    print("Value of :",x)
except NameError as ne:
    print(ne)

"""

# Explain which are errors and which are exceptions.

# **Task:**
# Handle only the runtime exceptions properly using try-except.


