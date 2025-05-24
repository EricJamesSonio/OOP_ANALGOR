from product import *
from typing import List
from abc import ABC, abstractmethod


class Inventory:
    def __init__(self):
        self.items: List["Base"] = []
        self.observers: List["Observer"] = []
        self.inventoryviewer = InventoryViewer(self)
        self.threshold = 10
        self.index_counter = 0

    def find_item(self, code):
        for item in self.items:
            if item.code == code:
                return item
        return None

    def add_item(self, item: Base):
        product = self.find_item(item.code)
        if product:
            product.quantity += item.quantity
            self.notify(
                {"action": "add_stock", "item": product, "quantity": product.quantity}
            )
        else:
            item.index = self.index_counter
            self.index_counter += 1

            self.items.append(item)
            self.notify({"action": "add_item", "item": item, "quantity": item.quantity})

    def remove_item(self, code):
        product = self.find_item(code)
        if product:
            self.items.remove(product)
            self.notify(
                {"action": "remove_item", "item": product, "quantity": product.quantity}
            )
        else:
            return None

    def update_stock(self, code, quantity):
        product = self.find_item(code)
        if product and quantity > 0:
            product.quantity += quantity
            self.notify(
                {
                    "action": "add_stock",
                    "item": product,
                    "quantity": product.quantity,
                    "added": quantity,
                }
            )
        elif product and quantity < 0:
            product.quantity += quantity
            self.notify(
                {
                    "action": "add_stock",
                    "item": product,
                    "quantity": product.quantity,
                    "removed": quantity,
                }
            )
        else:
            return None

    def add_observer(self, observer: "Observer"):
        self.observers.append(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)

    def display_items(self):
        self.inventoryviewer.display_items()

    def set_threshold(self, threshold):
        self.threshold = threshold

    def is_low_stock(self, item: Base):
        if item.quantity <= self.threshold:
            return True
        return False

    def check_stock(self):
        for item in self.items:
            if self.is_low_stock(item):
                self.notify(
                    {"action": "low_stock", "item": item, "quantity": item.quantity}
                )
        return None

    def display_items(self):
        self.inventoryviewer.display_items()


class IngredientInventory(Inventory):
    pass


class FoodMenuInventory(Inventory):
    def __init__(self):
        super().__init__()
        self.main_course = []
        self.dessert = []

    def get_category_by_parent(self, cls_name):
        return [item for item in self.items if isinstance(item, cls_name)]

    def main_course_item(self):
        self.main_course = self.get_category_by_parent(MainCourse)

    def dessert_item(self):
        self.dessert = self.get_category_by_parent(Dessert)

    def display_main_course(self):
        self.main_course_item()
        for item in self.main_course:
            print(item.get_details())

    def display_dessert(self):
        self.dessert_item()
        for item in self.dessert:
            print(item.get_details())


class InventoryViewer:
    def __init__(self, inventory: Inventory):
        self.inventory = inventory

    def display_items(self):
        for item in self.inventory.items:
            print(item.get_details())


class Observer(ABC):
    def __init__(self):
        self.records = []

    def update(self, message):
        pass


class Logger(Observer):
    pass


class StockAlertSystem(Observer):
    pass
