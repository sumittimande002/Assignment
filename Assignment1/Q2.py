# Program to Calculate Total Cost After Discount
# Problem Statement: Write a program to calculate the total cost after
# applying a discount. The program should take the original price and 
# discount percentage as input, and then calculate the price after applying 
# the discount.
OPrice = int(input("Enter a Original Price : "))
DPercentage = int(input("Enter a Discount Percentage : "))
FinalPrice = (OPrice - (DPercentage/100)*OPrice)
print("Final Price : ",int(FinalPrice))
