# string methods 

s = "Hii My Name is Sumit Timande am From Wardha"
print(s.capitalize()) #First  latter is capital from entire line

print(s.casefold()) # Convert into lower Case

s1 = "Sumit"

v = (s1.center(8)) # Space is add before and after the string
print(len(s1))
print(s1)
print(len(v))
print(v)

print(s.count("S")) # is used for counting the char in the string how many time it occur
print(s.count("a"))

print(s.encode())

print(s.endswith("Wardha")) #it's Check the string is end with given char or not if
              # ends with given char then it give True otherwise it will give False
print(s.endswith("a"))
print(s.endswith("s"))

s = "Rahul"
print(s.zfill(6)) # Add 0 Before the String i will give 6 in zfill then they first 
# count string len my string len is 5 and i will pass zfill 6 
# thats why its only one 0 is add 5 str 1 Zero total 6 

# s = "hii    R"
# print(s)
# print(len(s))
# s1 = s.expandtabs(2)
# print(s1)
# print(len(s1))

s = "Hii My Name is Sumit Timande am From Wardha"

print(s.find("Timande")) # find the index no of given char or string

print(s[-1].islower()) #it's check its lower or not

print(s[1].isupper())
print(s[0].isupper())
s = "Hii My Name is Sumit Timande am From Wardha 1"

print(s.isdigit()) #check its digit or not
print(s[-1].isdigit())

print(s.index("W"))# find index No

print("isdecimal")

d = "V = 10.20"
print(d[4].isdecimal()) 
print(s.isdecimal())

print("isdigit")

print(d.isdigit()) 
print(d[4].isnumeric())

