# 5.Write a program to count the number of digits in a given number using a loop.
number = int(input("Enter a Number : "))
# count = 0
# if number == 0:
#     count = 1
# else:
#     while number > 0:
#         number = number // 10
#         count += 1
# print("Count of Number : " ,count)
count = 0
if number == 0:
    count= 1
else:
    for i in number , 0:
        number = number//10
        count = count + 1
print("Count of number : ",count)
