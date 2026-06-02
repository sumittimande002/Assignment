# 6. ATM Withdrawal Simulation

# **Question:**
# Simulate ATM withdrawal:

# * Ask user for withdrawal amount
# * If amount > balance → raise error
# * Handle invalid input

amt = int(input("Enter Withdrawal amount : "))
balance = 5000
if amt > balance :
    print("Insufficient balance.")
else:
    print("Withdrawal successful. Remaining balance:",balance - amt)


# Balance = 5000

# **Test Case 1:**
# Input: 2000

# Output:
# Withdrawal successful. Remaining balance: 3000

# **Test Case 2:**
# Input: 6000

# Output:
# Error: Insufficient balance.
