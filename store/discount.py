from abc import ABC, abstractmethod


class Discount(ABC):
    @abstractmethod
    def apply_discount(self, price):
        pass


class PWDDiscount(Discount):
    def apply_discount(self, price):
        return price * 0.90


class SeniorDiscount(Discount):
    def apply_discount(self, price):
        return price * 0.88


class BulkDiscount(Discount):
    def apply_discount(self, price):
        if price >= 100:
            return price * 0.95
        else:
            return price
