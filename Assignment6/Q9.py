# 9.Write a program to demonstrate the use of break and continue statements
#  with a loop.

n = int(input("Enter a Number : "))
i = 1
while i <= n:
    if i == 5:
        break
    print(i)
    i += 1
print("------------------------")

k = int (input("Enter a Number : "))
while i <= k:
    if i == 10 :
        i += 1
        continue
    print(i)
    i +=1

