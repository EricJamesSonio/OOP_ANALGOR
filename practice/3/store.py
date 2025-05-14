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


class Appliances(Product):
    def __init__(self, name, code, price, quantity):
        super().__init__(name, code, price, quantity)

    def get_details(self):
        return f"Name : {self.name}, Code : {self.code}, Price : {self.price}, Quantity : {self.quantity}"


class SchoolSupllies(Product):
    def __init__(self, name, code, price, quantity):
        super().__init__(name, code, price, quantity)

    def get_details(self):
        return f"Name : {self.name}, Code : {self.code}, Price : {self.price}, Quantity : {self.quantity}"


class Inventory:
    def __init__(self):
        self.items: List[Product] = []
        self.observers: List["Observer"] = []

    def add_item(self, item: Product):
        for existing_item in self.items:
            if existing_item.code == item.code:
                existing_item.quantity += item.quantity
                return

        self.items.append(item)

    def find_item(self, code):
        for item in self.items:
            if item.code == code:
                return item
            return "Item Doesn't exist"

    def remove_item(self, code):
        item = self.find_item(code)
        if item:
            self.items.remove(item)
        else:
            return "Item Doesn't exist"

    def add_observer(self, observer: "Observer"):
        self.observers.append(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)


class Observer(ABC):
    def __init__(self):
        self.records = []

    @abstractmethod
    def update(self, message):
        pass


class Logger(Observer):
    def __init__(self):
        super().__init__()

    def update(self, message):
        pass


class StockAlertSystem(Observer):
    def __init__(self):
        super().__init__()

    def update(self, message):
        pass
