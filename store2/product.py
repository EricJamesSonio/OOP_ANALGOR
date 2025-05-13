from abc import ABC, abstractmethod
from typing import List, Optional


class Product(ABC):
    def __init__(self, name, code, price, quantity):
        self.name = name
        self.code = code
        self.price = price
        self.quantity = quantity

    @abstractmethod
    def get_details(self):
        pass

    @abstractmethod
    def price(self):
        pass


class Electronic(Product):
    def __init__(self, name, code, price, quantity):
        super().__init__(name, code, price, quantity)

    def get_details(self):
        return f"Name : {self.name}, Code : {self.code}, Price : {self.price}, Quantity : {self.quantity}"

    def price(self):
        return self.price


class Book(Product):
    def __init__(self, name, code, price, quantity):
        super().__init__(name, code, price, quantity)

    def get_details(self):
        return f"Name : {self.name}, Code : {self.code}, Price : {self.price}, Quantity : {self.quantity}"

    def price(self):
        return self.price


class Clothing(Product):
    def __init__(self, name, code, price, quantity):
        super().__init__(name, code, price, quantity)

    def get_details(self):
        return f"Name : {self.name}, Code : {self.code}, Price : {self.price}, Quantity : {self.quantity}"

    def price(self):
        return self.price


class Decorator(Product):
    def __init__(self, name, code, price, quantity):
        super().__init__(name, code, price, quantity)
        self.product = Product()

    @abstractmethod
    def get_details(self):
        pass

    @abstractmethod
    def price(self):
        pass
