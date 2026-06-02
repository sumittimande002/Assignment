# 11. Negative Number Not Allowed

# **Question:**
# Create custom exception:
class NegativeNumberError(Exception):
    pass
# ```
# NegativeNumberError
# ```
try :
    number = int(input("Enter a Number : "))
    if number > 0:
        raise NegativeNumberError ("User enters negative number ")
    print("Not Negative Number .")
except Exception as es:
    print(es)

# Raise exception if user enters negative number.
