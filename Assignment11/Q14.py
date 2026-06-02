# ### 14. Custom Exception with finally Block

# **Question:**
# Create custom exception:
class PasswordLengthError(Exception):
    pass


try:
    password = input("Enter a Password : ")
    if password < 6:
        raise PasswordLengthError("Password must be Gretter then 6 char")
    



# ```
# PasswordLengthError
# ```

# If password length < 6 → raise exception
# Ensure finally block always prints:
# "Validation process completed."
