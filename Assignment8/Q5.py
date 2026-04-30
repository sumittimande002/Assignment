# ### 5. create_account(name, role="User")

# **Question:**
# Create a function with default role.
def create_account(name , role = "user"):
    print(f"Account created for {name} with role {role}")


create_account("Rahul")
create_account("AdminUser","Admin")


# **Test Case 1:**
# Input:
# create_account("Rahul")

# Expected Output:
# Account created for Rahul with role User

# **Test Case 2:**
# Input:
# create_account("AdminUser", "Admin")

# Expected Output:
# Account created for AdminUser with role Admin