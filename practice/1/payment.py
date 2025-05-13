from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass
    
class CreditCardPayment(PaymentStrategy):
    def process_payment(self, amount):
        fee = amount * 0.10
        total_amount = amount + fee
        print(f"Processing credit card payment of ${total_amount} (including 10% fee)")
        return f"Paid ${total_amount} by Credit Card (including 10% fee)"

    
class CashPayment(PaymentStrategy):
    def process_payment(self, amount):
        print(f"Processing cash payment of ${amount}")
        return f"Paid ${amount} by Cash"
