## 8. Program to Convert Minutes to Hours and Minutes

# **Problem Statement:** Write a program to convert total minutes into hours and remaining minutes.

min = int(input("Enter a Min : "))
hr_result = min / 60
min_result = min % 60
print(f"{int(hr_result)} Hours {min_result} Minutes")