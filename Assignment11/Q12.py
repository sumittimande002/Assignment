# 12. Student Marks Validation

# **Question:**
# Create custom exception:
class InvalidMarksError(Exception):
    pass
# ```
# InvalidMarksError
# ```
try :
    mark = int (input("Enter a Mark : "))
    if mark > 0 and mark <100:
        print("Valid Marks.")
    else:
        raise InvalidMarksError("Mark shoud Between 0 to 100")
except Exception as es:
    print(es)


# Marks should be between 0 and 100.

# **Test Case 1:**
# Input: 85
# Output: Valid marks.

# **Test Case 2:**
# Input: 120
# Output: InvalidMarksError: Marks must be between 0 and 100.
