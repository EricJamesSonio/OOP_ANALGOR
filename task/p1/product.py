from abc import ABC, abstractmethod
from typing import List


class Product:
    def __init__(self, name, code, quantity, price):
        self.name = name
        self.code = code
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"Name : {self.name}, Code : {self.code}, Quantity : {self.quantity}, Price : {self.price}"


class OrderItem:
    def __init__(self, product: Product):
        self.product = product
