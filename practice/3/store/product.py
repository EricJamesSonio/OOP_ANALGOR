from abc import ABC, abstractmethod


class Product(ABC):
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    @abstractmethod
    def get_type(self):
        pass


class DigitalProduct(Product):
    def get_type(self):
        return "Digital"


class PhysicalProduct(Product):
    def get_type(self):
        return "Physical"
