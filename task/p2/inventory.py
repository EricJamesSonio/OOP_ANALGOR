from products import Product
from typing import List
from abc import ABC, abstractmethod


class Inventory:
    def __init__(self):
        self.items: List[Product] = []
        self.inventoryviewer = InventoryViewer(self)
        self.observer: List["Observer"] = []

    def find_item(self, code):
        for item in self.items:
            if item.code == code:
                return item
        return None

    def add_item(self, item):
        product = self.find_item(item.code)
        if product:
            product.quantity += item.quantity
        else:
            self.items.append(item)

    def remove_item(self, code):
        product = self.find_item(code)
        if product:
            self.items.remove(product)
        else:
            return None

    def update_stock(self, code, quantity):
        product = self.find_item(code)
        if product:
            product.quantity += quantity
        else:
            return None

    def display_items(self):
        self.inventoryviewer.display_items()

    def add_observer(self, observer: "Observer"):
        self.observer.append(observer)

    def notify(self, message):
        pass


class InventoryViewer:
    def __init__(self, inventory: Inventory):
        self.inventory = inventory

    def display_items(self):
        for item in self.inventory.items:
            print(item.get_details())


class Observer(ABC):
    def __init__(self):
        self.records = []

    @abstractmethod
    def update(self, message):
        pass
