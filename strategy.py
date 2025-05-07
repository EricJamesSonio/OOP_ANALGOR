from abc import ABC, abstractmethod
from typing import List, Optional


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Name : {self.name} , Price : {self.price}"


class Discount(ABC):
    @abstractmethod
    def apply_discount(self, price):
        pass


class SeasonalDiscount(Discount):
    def apply_discount(self, price):
        return price * 0.90


class HolidayDiscount(Discount):
    def apply_discount(self, price):
        return price * 0.80


class LoyaltyDiscount(Discount):
    def apply_discount(self, price):
        return price * 0.95


class BulkDiscount(Discount):
    def apply_discount(self, price):
        if price > 100:
            return price * 0.85
        else:
            return price


class Cart:
    def __init__(self, discount: Discount):
        self.discount = discount
        self.items: List[Item] = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_totals(self):
        total = 0
        for item in self.items:
            total += item.price

        return self.discount.apply_discount(total)


item1 = Item("Milo", 200)
item2 = Item("BearBrand", 300)
item3 = Item("Drinks", 500)

cart = Cart(BulkDiscount())

cart.add_item(item1)
print(cart.calculate_totals())
