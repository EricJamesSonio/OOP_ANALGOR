from abc import ABC, abstractmethod
from typing import List, Optional

# ------------------------- Base Class --------------------------- #


class FoodItem:
    def __init__(self, name, id, price, quantity):
        self.name = name
        self.id = id
        self.price = price
        self.quantity = quantity

    def get_details(self):
        return f"Name: {self.name}, ID: {self.id}, Price: {self.price}, Quantity: {self.quantity}"


# ------------------------- Shared Price Control Mixin --------------------------- #


class PriceControlledItem(FoodItem):
    price = 0

    def __init__(self, name, id, quantity):
        super().__init__(name, id, self.__class__.price, quantity)

    @classmethod
    def set_price(cls, new_price):
        cls.price = new_price

    @classmethod
    def get_price(cls):
        return cls.price


# ------------------------- Chicken Wings --------------------------- #


class ChickenWings(PriceControlledItem):
    pass


class FriedChickenWings(ChickenWings):
    price = 120


class BakedBuffaloWings(ChickenWings):
    price = 150


class BBQChickenWings(ChickenWings):
    price = 150


class DryRubChickenWings(ChickenWings):
    price = 150


class HoneySrirachaWings(ChickenWings):
    price = 160


class LemonPepperWings(ChickenWings):
    price = 150


# ------------------------- Fries --------------------------- #


class Fries(PriceControlledItem):
    pass


class CheeseFries(Fries):
    price = 100


class garlicFries(Fries):
    price = 100


class BelgianFries(Fries):
    price = 110


class StandardCut(Fries):
    price = 70


class SweetPotatoFries(Fries):
    price = 75


class TruffleFries(Fries):
    price = 160


# ------------------------- Pizza --------------------------- #


class Pizza(PriceControlledItem):
    pass


class PepperoniPizza(Pizza):
    price = 85


class HamCheesePizza(Pizza):
    price = 90


class TomatoOlivePizza(Pizza):
    price = 90


class HawaiianPizza(Pizza):
    price = 80


class PacificVeggie(Pizza):
    price = 100


# ------------------------- Drinks --------------------------- #


class Drinks(PriceControlledItem):
    pass


class Coke(Drinks):
    price = 120


class IcedTea(Drinks):
    price = 110


class WaterBottle(Drinks):
    price = 20


class OrangeJuice(Drinks):
    price = 75


class Sprite(Drinks):
    price = 120


class SpriteZero(Drinks):
    price = 35
