# 6. product price calculator (functions + default and keywords)

def calculate_price(Product_price,Tax_per = 0.10 ,Discount_amt = 40 ):
    tax_amount = (Product_price * Tax_per )/ 100
    total_price =( Product_price+ tax_amount) - Discount_amt
    print (total_price)


calculate_price(1000 )
calculate_price(4000, Discount_amt=500,Tax_per=20)