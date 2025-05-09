from abc import ABC, abstractmethod
from typing import List, Optional


class Product(ABC):
    def __init__(self, name, code, price, quantity, exp_date, size):
        self.name = name
        self.code = code
        self.price = price
        self.quantity = quantity
        self.exp_date = exp_date
        self.size = size

    def get_details(self):
        return f"Name : {self.name}, Code : {self.code}, Price : {self.price}, Quantity : {self.quantity}, Exp_date : {self.exp_date}, Size : {self.size}"


class DigitalProduct(Product):
    def __init__(self, name, code, price, quantity, exp_date, size):
        super().__init__(name, code, price, quantity, exp_date, size)

    def get_details(self):
        return f"[Digital] " + super().get_details()


class PhysicalProduct(Product):
    def __init__(self, name, code, price, quantity, exp_date, size):
        super().__init__(name, code, price, quantity, exp_date, size)

    def get_details(self):
        return f"[Physical] " + super().get_details()
