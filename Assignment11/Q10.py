# Bank Minimum Balance Exception

# **Question:**
# Create custom exception:
class MinimumBalanceError(Exception):
    pass 
# ```
# MinimumBalanceError
# ```

try :
    balance = 2000
    withh = int(input("Enter a amount :"))
    remining_balance = balance - withh
    if remining_balance < 1000:
        raise MinimumBalanceError("Minimum Balance is requred.")
    print("You can Move for transaction.")
except Exception as es:
    print(es)

# If withdrawal makes balance < 1000 → raise exception.
