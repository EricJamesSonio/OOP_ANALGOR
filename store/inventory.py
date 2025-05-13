from abc import ABC, abstractmethod
from typing import List, Optional
from product import *
from printer import *


class Inventory:
    def __init__(self):
        self.items: List[Product] = []
        self.observers: List[Observer] = []

    def add_item(self, item: Product):
        for existing_item in self.items:
            if existing_item.id == item.id:
                existing_item.quantity += item.quantity
                self.notify(
                    {"action": "addStock", "item": item.name, "qtty": item.quantity}
                )

        self.items.append(item)
        self.notify({"action": "addItem", "item": item.name, "qtty": item.quantity})

    def remove_item(self, item: Product):
        for existing_item in self.items:
            if existing_item.id == item.id:
                self.items.remove(existing_item)
                self.notify(
                    {"action": "removeItem", "item": item.name, "qtty": item.quantity}
                )

    def find_item(self, id):
        for item in self.items:
            if item.id == id:
                return item
            return None

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)

    def add_observer(self, observer: "Observer"):
        self.observers.append(observer)


class InventoryViewer:
    def __init__(self, inventory: Inventory):
        self.inventory = inventory

    def display(self):
        for item in self.inventory.items:
            Printer.print_message(item.get_details())


class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass


class Logger(Observer):
    def update(self, message):
        if message["action"] == "addItem":
            item = message["item"]
            qtty = message["qtty"]
            return f"Item : {item} Qtty : {qtty} Added to our inventory!"
        elif message["action"] == "removeItem":
            item = message["item"]
            qtty = message["qtty"]
            return f"Item : {item} Qtty : {qtty} Remove from the inventory! "


class StockAlertSystem(Observer):
    def update(self, message):
        if message["action"] == "addStock":
            item = message["item"]
            qtty = message["qtty"]
            return f"Item : {item} Qtty : {qtty} Added Stock!"
        else:
            return
