# ## SECTION 4: INTERMEDIATE LOGIC-BASED EXCEPTION HANDLING

# ### 13. Nested Try-Except Block

# **Question:**
# Create program:

# * Take number input
try :
    number = int(input("Enter a Number : "))
    div = 100 / number
    print("division of 100 by ",number," is : ",div)

    try :
        num = int(input("Enter Second Number : "))
        print("You Entered : ",num)
    except ValueError as ve:
        print("Value Error : ",ve)
except ValueError as ve:
        print("Value Error : ",ve)
except ZeroDivisionError as zs:
         print("Zero Division Error : ", zs)
# * Divide 100 by number
# * Inside that, convert another input to integer
# * Use nested try-except

# Handle:

# * ZeroDivisionError
# * ValueError
