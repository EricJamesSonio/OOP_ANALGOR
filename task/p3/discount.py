from abc import ABC, abstractmethod


class Discount:
    @abstractmethod
    def discount_percent(self):
        pass


class PWDDiscount(Discount):
    def discount_percent(self):
        return 0.90


class SeniorDiscount(Discount):
    def discount_percent(self):
        return 0.80
