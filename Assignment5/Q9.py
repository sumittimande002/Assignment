# 9.Write a program to remove leading and trailing spaces from a string.


ch = input("Enter a String : ")
print("Before removing : ",len(ch))
after = ch.strip()
print("Remove leading and trailing spaces :",after)
print("After Removing : ",len(after))