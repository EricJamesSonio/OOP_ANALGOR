from product import *
from typing import List


class Inventory:
    def __init__(self):
        self.items: List[ProductItem] = []
        self.inventoryviewer = InventoryViewer(self)

    def find_item(self, id):
        for item in self.items:
            if item.id == id:
                return item
        return None

    def add_item(self, item: ProductItem):
        product = self.find_item(item.id)
        if product:
            product.quantity += item.quantity
        else:
            self.items.append(item)

    def remove_item(self, id):
        product = self.find_item(id)
        if product:
            self.items.remove(product)
        else:
            return None

    def reduce_stock(self, id, quantity):
        product = self.find_item(id)
        if product:
            product.quantity -= quantity
            if product.quantity <= 0:
                self.items.remove(product)

        return None

    def increase_stock(self, id, quantity):
        product = self.find_item(id)
        if product:
            product.quantity += quantity
        else:
            return None

    def display_items(self):
        self.inventoryviewer.display_items()


class InventoryViewer:
    def __init__(self, inventory: Inventory):
        self.inventory = inventory

    def display_items(self):
        for item in self.inventory.items:
            print(item.get_details())
