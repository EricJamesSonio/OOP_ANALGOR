from product import ProductItem
from typing import List
from abc import ABC, abstractmethod


class Inventory:
    def __init__(self):
        self.items: List["ProductItem"] = []
        self.inventoryviewer = InventoryViewer(self)
        self.logger = Logger()
        self.stockalert = StockAlertSystem()
        self.observers: List["Observer"] = [self.logger, self.stockalert]

    def add_item(self, item: ProductItem):
        product = self.find_item(item.id)
        if product:
            product.quantity += item.quantity
            self.notify(
                {
                    "action": "add_stock",
                    "item": product,
                    "added": item.quantity,
                    "total": product.quantity,
                }
            )
        else:
            self.items.append(product)
            self.notify(
                {"action": "add_item", "item": product, "total": product.quantity}
            )

    def find_item(self, id):
        for item in self.items:
            if item.id == id:
                return item
        return None

    def remove_item(self, id):
        product = self.find_item(id)
        if product:
            self.items.remove(product)
            self.notify(
                {"action": "removed_item", "item": product, "total": product.quantity}
            )
        else:
            return None

    def update_stock(self, id, quantity):
        product = self.find_item(id)
        if product and quantity > 0:
            product.quantity += quantity
            self.notify(
                {
                    "action": "add_stock",
                    "item": product,
                    "added": quantity,
                    "total": product.quantity,
                }
            )
        elif product and quantity < 0:
            product.quantity += quantity
            self.notify(
                {
                    "action": "reduced_stock",
                    "item": product,
                    "added": quantity,
                    "total": product.quantity,
                }
            )
        else:
            return None

    def display_items(self):
        self.inventoryviewer.display_items()

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)


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


class Logger(Observer):
    pass


class StockAlertSystem(Observer):
    pass
