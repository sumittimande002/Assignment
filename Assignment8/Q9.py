# ### 9. Palindrome Checker

# **Question:**
# Create function is_palindrome(word).

def is_palindrome(word):
    if(word == word[::-1]):
        return True
    else :
        return False
    
print(is_palindrome("madam"))
# Return True if palindrome else False.

# **Test Case 1:**
# Input:
# is_palindrome("madam")

# Expected Output:
# True

# **Test Case 2:**
# Input:
# is_palindrome("python")

# Expected Output:
# False