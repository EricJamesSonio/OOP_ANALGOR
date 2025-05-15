from abc import ABC, abstractmethod


class Order:
    def __init__(self, order_type: "Payment", amount):
        self.order_type = order_type
        self.amount = amount

    def calculate_shipping(self):
        return self.order_type.pay(self.amount)

    def total_amount(self):
        return self.amount + self.calculate_shipping()


class Payment(ABC):
    @abstractmethod
    def calculate_shipping(self, amount):
        pass


class Online(Payment):
    def calculate_shipping(self, amount):
        return amount * 0.1


class Walkin(Payment):
    def calculate_shipping(self, amount):
        return 0


class PickUp(Payment):
    def calculate_shipping(self, amount):
        return amount * 0.05
