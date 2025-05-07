from abc import ABC, abstractmethod
from typing import List, Optional


class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass


class StockAlertSystem(Observer):
    def update(self, message):
        if message["action"] == "new_item":
            item = message["item"]
            return f"Notification! New item : {item} with qtty : {quantity} was added to our Stock!"
        elif message["action"] == "add_stock":
            item = message["item"]
            quantity = message["quantity"]
            return f"Notification! Stock {quantity} was added to our item {item}!"


class Logger(Observer):
    def update(self, message):
        return f"Notified {message}"


class StoreItem(ABC):
    def __init__(self, name, code, price, quantity):
        self.name = name
        self.code = code
        self.price = price
        self.quantity = quantity

    @abstractmethod
    def get_details(self):
        pass


class Guitar(StoreItem):
    def __init__(self, name, code, price, quantity, type):
        super().__init__(name, code, price, quantity)
        self.type = type

    def get_details(self):
        return f"Name : {self.name}, Code : {self.code}, Price : {self.price}, Quantity : {self.quantity}, Type : {self.type}"


class GuitarPedal(StoreItem):
    def __init__(self, name, code, price, quantity, effects):
        super().__init__(name, code, price, quantity)
        self.effects = effects

    def get_details(self):
        return f"Name : {self.name}, Code : {self.code}, Price : {self.price}, Quantity : {self.quantity}, Effects : {self.effects}"


class StockManager:
    def __init__(self):
        self.items: List["StoreItem"] = []
        self.observers: List["Observer"] = []

    def add_item(self, item: StoreItem, quantity):
        for exist in self.items:
            if exist.code == item.code:
                item.quantity += quantity
                self.notify(item)
                return
        self.items.append(item)
        self.notify({"action": "add_item", "item": item, "quantity": quantity})

    def add_stock(self, code, quantity):
        for item in self.items:
            if item.code == code:
                item.quantity += quantity
                self.notify({"action": "new_item", "item": code, "quantity": quantity})
                return
        return f"Item with code : {code} does'nt exist"

    def add_observer(self, system):
        self.observers.append(system)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)

    def display_items(self):
        for item in self.items:
            print(item.get_details())


store = StockManager()
logger = Logger()
alert = StockAlertSystem()

store.add_observer(logger)
store.add_observer(alert)

item1 = Guitar("Fender", 123, 200, 2, "Electric")
item2 = GuitarPedal("Fender", 345, 100, 2, "Distortion")

store.add_item(item1, 2)
store.add_item(item2, 2)

store.display_items()
