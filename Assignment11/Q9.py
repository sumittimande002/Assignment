# 9. Custom Login Exception

# **Question:**
# Create custom exception:

class LoginError(Exception):
    pass

# ```
# LoginError
# ```

# Raise if username is incorrect.
correct_username = "Sumit@123"
try :
    username = input("Enter a User Name : ")
    if correct_username != username:
        raise LoginError ("Invalid username")
    print("Correct Username.")
except Exception as es:
    print(es)

# Expected Output Example:
# LoginError: Invalid username
