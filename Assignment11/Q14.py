# ### 14. Custom Exception with finally Block

# **Question:**
# Create custom exception:
class PasswordLengthError(Exception):
    pass


try:
    password = input("Enter a Password : ")
    if len(password) < 6:
        raise PasswordLengthError("Password must be Gretter then 6 char")
    else:
         print("Password is valid.")
except PasswordLengthError as e:
        print(e)
finally:
        print("Validation process completed.")
    



# ```
# PasswordLengthError
# ```

# If password length < 6 → raise exception
# Ensure finally block always prints:
# "Validation process completed."
