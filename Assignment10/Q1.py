# # 1. password checker (functions , loops , conditional statements)

# ## 1. Password Checker

# **Concepts Covered:**
# Functions, Loops, Conditional Statements

# ### Problem Statement

# Create a Python program that checks whether a given password is **strong or weak** based on predefined security rules. Password validation is a common requirement in modern applications such as banking systems, social media platforms, and enterprise software.

# ### Requirements

# The program should perform the following validations:

# 1. The password must be **at least 8 characters long**.
# 2. It must contain **at least one uppercase letter**.
# 3. It must contain **at least one lowercase letter**.
# 4. It must contain **at least one numeric digit (0-9)**.
# 5. It must contain **at least one special character** (such as `@`, `#`, `$`, `%`, `!`, etc.).

# ### Implementation Guidelines

# * Create a **function** named `password_checker()`.
import string
def password_checker(password):
    l = ["@", "#", "&", "*", "!"]
    if (
        any (char.isupper() for char in password) and 
        any (char.islower() for char in password) and
        any (char.isdigit() for char in password) and
        any (char in l for char in password) and
        (len(password) >= 8)
        ):
        print("Password is Strong")
    else:
        print("Password is Weak")


password = input("Enter a Password : ")
password_checker(password)

# print(string.punctuation)





# * Accept the password as input from the user.
# * Use a **loop** to iterate through each character in the password.
# * Use **conditional statements** to check the required conditions.
# * Return whether the password is **Strong** or **Weak**.

# ### Expected Outcome

# The program should display a message indicating whether the password satisfies all security requirements.
