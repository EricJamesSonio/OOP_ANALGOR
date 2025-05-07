from abc import ABC, abstractmethod
from typing import List, Optional


class FoodItem(ABC):
    def __init__(self, name, type, flavor, size):
        self.name = name
        self.type = type
        self.flavor = flavor
        self.size = size

    @abstractmethod
    def get_details(self):
        pass


class Burger(FoodItem):
    def __init__(self, name, type, flavor, size, add_ons):
        super().__init__(name, type, flavor, size)
        self.add_ons = add_ons

    def get_details(self):
        return f"Name : {self.name}, Type : {self.type}, Flavor : {self.flavor}, Size : {self.size}, Add ons : {self.add_ons}"


class Pizza(FoodItem):
    def __init__(self, name, type, flavor, size, spices):
        super().__init__(name, type, flavor, size)
        self.spices = spices

    def get_details(self):
        return f"Name : {self.name}, Type : {self.type}, Flavor : {self.flavor}, Size : {self.size}, spices : {self.spices}"


class FoodFactory:

    def helper(self):
        name = input("Name : ")
        type = input("Type : ")
        flavor = input("Flavor : ")
        size = input("Size : ")
        return name, type, flavor, size

    def create(self, food_type):
        if food_type == "Pizza":
            name, type, flavor, size = self.helper()
            spices = input("Spices : ")
            return Pizza(name, type, flavor, size, spices)
        elif food_type == "Burger":
            name, type, flavor, size = self.helper()
            addons = input("Add_ons : ")
            return Burger(name, type, flavor, size, addons)
        else:
            return f"Food type {food_type} does'nt exist"
