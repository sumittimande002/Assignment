# ### 7. Login System with Limited Attempts

# **Question:**
# Create login system:
correct_password = "admin123"
id = input("Enter a Login Id :")
att = 0
while att < 3:
    password = input("Enter a Password : ")


    try:
        if password == correct_password :
            print("Login Successful.")
            break
        else:
            att +=1
            print("wrong password your left Attempts.",3 - att)
            if att == 3:
                print("Access denied after 3 failed attempts")
            
    except Exception as e:
            print(e)

# * Correct password = "admin123"
# * Allow only 3 attempts
# * Raise exception after 3 failed attempts

# Expected Output:
# Access denied after 3 failed attempts.

