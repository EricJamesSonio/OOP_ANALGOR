from abc import ABC, abstractmethod


class Discount(ABC):
    @abstractmethod
    def percent_discount(self):
        pass


class PWDDiscount(Discount):
    def percent_discount(self):
        return 0.95


class SeniorDiscount(Discount):
    def percent_discount(self):
        return 0.80
