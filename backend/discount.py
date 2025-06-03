from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    def __init__(self):
        self.discount_percent = 0

    @abstractmethod
    def apply_discount(self, price):
        pass


class PWDDiscount(DiscountStrategy):
    def __init__(self):
        self.discount_percent = 0.90

    def apply_discount(self, price):
        return price * self.discount_percent


class SeniorDiscount(DiscountStrategy):
    def __init__(self):
        self.discount_percent = 0.85

    def apply_discount(self, price):
        return price * self.discount_percent
