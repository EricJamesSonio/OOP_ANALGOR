from abc import ABC, abstractmethod
from typing import List, Optional


class StoreItem(ABC):
    def __init__(self, name, code, price, discount_rate):
        self.name = name
        self.code = code
        self.price = price
        self.discount_rate = discount_rate

    @abstractmethod
    def calculate_totals(self):
        pass


class FoodItem(StoreItem):
    def __init__(
        self, name, code, price, discount_rate, ingredients_list, item_type="Food"
    ):
        super().__init__(name, code, price, discount_rate)
        self.ingredients_list = ingredients_list
        self.item_type = item_type

    def calculate_totals(self):
        return self.price * (1 - self.discount_rate)


class DrinkItem(StoreItem):
    def __init__(self, name, code, price, discount_rate, volume, item_type="Drink"):
        super().__init__(name, code, price, discount_rate)
        self.volume = volume
        self.item_type = item_type

    def calculate_totals(self):
        return self.price * (1 - self.discount_rate)


class DessertItem(StoreItem):
    def __init__(self, name, code, price, discount_rate, flavor, item_type="Dessert"):
        super().__init__(name, code, price, discount_rate)
        self.flavor = flavor
        self.item_type = item_type

    def calculate_totals(self):
        return self.price * (1 - self.discount_rate)


class ItemFactory:
    def __init__(self):
        self.items = {
            "Food": self.createfood,
            "Dessert": self.createdessert,
            "Drinks": self.createdrinks,
        }

    def helper(self):
        print("<-- Helper Function -->")
        name = input("Name : ")
        code = input("Code : ")
        price = input("Price : ")
        discount_rate = input("Discount rate : ")
        return name, code, price, discount_rate

    def createitem(self, item_type):
        create = self.items.get(item_type)
        if not create:
            raise ValueError("Unknown type")
        return create()

    def createfood(self):
        name, code, price, discount_rate = self.helper()
        ingredients_list = input("Ingredients : ").split(",")
        return FoodItem(name, code, price, discount_rate, ingredients_list)

    def createdessert(self):
        name, code, price, discount_rate = self.helper()
        flavor = input("Flavor : ")
        return DessertItem(name, code, price, discount_rate, flavor)

    def createdrinks(self):
        name, code, price, discount_rate = self.helper()
        volume = float(input("Volume : "))
        return DessertItem(name, code, price, discount_rate, volume)
