from baseproduct import *
from observer import *
from typing import List


class Inventory:
    def __init__(self):
        self.items: List[ProductBase] = []
        self.observers: List[Observer] = []

    def find_item(self, code):
        for item in self.items:
            if item.code == code:
                return item
        return None

    def add_item(self, item):
        product = self.find_item(item.code)
        if product:
            product.quantity += item.quantity
            self.notify(
                {
                    "action": "add_stock",
                    "item": product,
                    "quantity": item.quantity,
                    "total": product.quantity,
                }
            )
        else:
            self.items.append(item)
            self.notify({"action": "add_item", "item": item, "quantity": item.quantity})

    def remove_item(self, code):
        product = self.find_item(code)
        if product:
            self.items.remove(product)
            self.notify(
                {
                    "action": "removed_item",
                    "item": product,
                    "quantity": product.quantity,
                }
            )
        else:
            return None

    def update_stock(self, code, quantity):
        product = self.find_item(code)
        if product and quantity < 0:
            product.quantity -= quantity
            self.notify(
                {
                    "action": "minus_stock",
                    "item": product,
                    "quantity": product.quantity,
                    "update": quantity,
                }
            )
        elif product and quantity > 0:
            product.quantity += quantity
            self.notify(
                {
                    "action": "add_stock",
                    "item": product,
                    "quantity": quantity,
                    "total": product.quantity,
                }
            )
        else:
            return None

    def add_observer(self, observer: Observer):
        self.observers.append(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)


class IngredientsInventory(Inventory):
    pass


class BeverageInventory(Inventory):
    pass


class InventoryViewer:
    def __init__(self, inventory: Inventory):
        self.inventory = inventory

    def display_inventory(self):
        for item in self.inventory.items:
            print(item.get_details())
