class InvalidCardNumberError(Exception):
    pass

class InsufficientBalsnaceError(Exception):
    pass   

class InvalidAmountError(Exception):
    pass
try:
    card_number = (input("Enter a Credit Card Number : "))
    amount = int(input("Enter the amount to be paid : "))
    if len(card_number) == 16:
        raise InvalidCardNumberError("Invalid Card Number. Card number must be 16 digits.")
    elif amount <= 0:
        raise InsufficientBalsnaceError("Invalid Amount. Amount must be greater than zero.")
    elif amount.isnumeric() == False:
        raise InvalidAmountError("Enter Balance in Number .")
    else:
        print("Payment successful.")
except Exception as es:
    print(es)
finally:
    print("Transaction Completed. ")