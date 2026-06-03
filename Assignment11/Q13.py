#  SECTION 4: INTERMEDIATE LOGIC-BASED EXCEPTION HANDLING

# ### 13. Nested Try-Except Block

# **Question:**
# Create program:
try :
    number = int(input("Enter a Number : "))
    div = 100/ number
    print("Division : ",div)
    try:
        another_number = int(input("Enter a Another Number : "))
        print("Another Number : ",another_number)
    except ValueError as ve:
        print(ve)
except ZeroDivisionError as es :
        print(es)
except ValueError as ve:
        print(ve)





# * Take number input
# * Divide 100 by number
# * Inside that, convert another input to integer
# * Use nested try-except

# Handle:

# * ZeroDivisionError
# * ValueError
