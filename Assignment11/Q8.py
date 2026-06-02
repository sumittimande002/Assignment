# 8. Custom Age Validation Exception

# **Question:**
# Create custom exception:

class InvalidAgeError (Exception):
    pass


# ```
# InvalidAgeError
# ```
try :
    age = int(input("Enter a Age :"))
    if age < 18:
       raise InvalidAgeError ("Age must be 18 or above")
    print("Access granted.")
except Exception as es:
    print(es)




# If age < 18 → raise exception.

# **Test Case 1:**
# Input: 20
# Output: Access granted.

# **Test Case 2:**
# Input: 15
# Output: InvalidAgeError: Age must be 18 or above.
