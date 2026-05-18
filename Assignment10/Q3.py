# 3. simple payment system (abstraction+overriding)

from abc import ABC , abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass
       

class CreditCardPayment(Payment):
    def pay(self):
        print("Payment Via Credit Card")

class UPIPayment(Payment):
    def pay(self):
        print("Payment Via UPI Payment")

class DebitCardPayment(Payment):
    def pay(self):
        print("Payment Via Debit Card")


class  NetBanking(Payment):
     def pay(self):
        print("Payment Via Net Banking")




c = CreditCardPayment()
c.pay()
u = UPIPayment()
u.pay()
d = DebitCardPayment()
d.pay()
n = NetBanking()
n.pay()
