from abc import ABC, abstractmethod
from typing import List, Optional


class Drink(ABC):
    def __init__(self, flavor):
        self.flavor = flavor

    @abstractmethod
    def get_details(self):
        pass

    @abstractmethod
    def price(self):
        pass


class Espresso(Drink):
    def __init__(self, flavor="Espresso"):
        super().__init__(flavor)

    def get_details(self):
        return f"Flavor : {self.flavor}"

    def price(self):
        return 100


class Latte(Drink):
    def __init__(self, flavor="Latte"):
        super().__init__(flavor)

    def get_details(self):
        return f"Flavor : {self.flavor}"

    def price(self):
        return 150


class DrinkDecorator(Drink):
    def __init__(self, drink: Drink):
        super().__init__(drink.flavor)
        self._drink = drink

    def get_details(self):
        pass

    def price(self):
        pass


class Milk(DrinkDecorator):
    def get_details(self):
        return self._drink.get_details() + ". Milk "

    def price(self):
        return self._drink.price() + 50


class WhippedCream(DrinkDecorator):
    def get_details(self):
        return self._drink.get_details() + ". WhippedCream "

    def price(self):
        return self._drink.price() + 20


class Sugar(DrinkDecorator):
    def get_details(self):
        return self._drink.get_details() + ". Sugar "

    def price(self):
        return self._drink.price() + 10


class ChocolateSyrup(DrinkDecorator):
    def get_details(self):
        return self._drink.get_details() + ". ChocolateSyrup "

    def price(self):
        return self._drink.price() + 30


coffee = Latte()
coffee = Milk(coffee)
print(coffee.price())
coffee = ChocolateSyrup(coffee)
print(coffee.price())
coffee = Sugar(coffee)
print(coffee.price())
