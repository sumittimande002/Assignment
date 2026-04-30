# ### 2. User-Defined Max, Min, Sum (Without Built-ins)

# **Question:**
input1 = [4, 8, 1, 9]
input2 = [-5, -2, -10]

# * Maximum
def max(par):
    max_Value = par[0]
    for i in par :
        if max_Value < i :
            max_Value = i
    return max_Value
        
print("Maximum : ",max(input1))

def min(val):
    min_val = val[0]
    for i in val :
        if min_val > i :
            min_val = i
    return min_val

print("Minimum : ",min(input1))


def sum(val):
    sum1 = 0
    for i in val:
        sum1 = sum1 +i
    return sum1

print("Sum : ",sum(input1))
    
# * Minimum
# * Sum

# Do NOT use max(), min(), sum().

# **Test Case 1:**
# Input:
# [4, 8, 1, 9]

# Expected Output:
# Maximum: 9
# Minimum: 1
# Sum: 22

# **Test Case 2:**
# Input:
# [-5, -2, -10]

# Expected Output:
# Maximum: -2
# Minimum: -10
# Sum: -17

