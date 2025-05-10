from abc import ABC, abstractmethod
from typing import List, Optional


class Product(ABC):
    def __init__(self, name, code, price, quantity):
        self.name = name
        self.price = price
        self.code = code
        self.quantity = quantity

    @abstractmethod
    def get_details(self):
        pass


class Burger(Product):
    def __init__(self, name, code, price, quantity):
        super().__init__(name, code, price, quantity)
        self.type = "Burger"

    def get_details(self):
        return f"Name : {self.name}, Code : {self.code}, Price : {self.price}, Quantity : {self.quantity}"


class Pizza(Product):
    def __init__(self, name, code, price, quantity):
        super().__init__(name, code, price, quantity)
        self.type = "Pizza"

    def get_details(self):
        return f"Name : {self.name}, Code : {self.code}, Price : {self.price}, Quantity : {self.quantity}"


class Fries(Product):
    def __init__(self, name, code, price, quantity):
        super().__init__(name, code, price, quantity)
        self.type = "Fries"

    def get_details(self):
        return f"Name : {self.name}, Code : {self.code}, Price : {self.price}, Quantity : {self.quantity}"


class Helper:
    @staticmethod
    def base_details():
        name = input("Name : ")
        code = input("Code : ")
        price = input("Price : ")
        quantity = input("Quantity : ")

        return name, code, price, quantity


class ProductFactory:
    def create(self, product_type):
        name, code, price, quantity = Helper.base_details()
        if product_type == "Burger":
            return Burger(name, code, price, quantity)
        elif product_type == "Fries":
            return Fries(name, code, price, quantity)

        elif product_type == "Pizza":
            return Pizza(name, code, price, quantity)
        else:
            return "Invalid product type!"
