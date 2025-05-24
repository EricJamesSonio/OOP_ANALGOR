from abc import ABC, abstractmethod
from typing import List, Optional
from datetime import datetime


class Product:
    def __init__(self, name, code, price, quantity, supplier, unit):
        self.name = name
        self.code = code
        self.price = price
        self.quantity = quantity
        self.supplier = supplier
        self.unit = unit

    def get_details(self):
        return f"Name : {self.name}, Code : {self.code}, Price : {self.price}, Quantity : {self.quantity}, Supplier : {self.supplier}"


class Inventory:
    def __init__(self):
        self.items: List["Product"] = []
        self.inventoryviewer = InventoryViewer(self)
        self.observers: List[Observer] = []
        self.threshold = 10

    def add_item(self, item):
        product = self.find_item(item.code)
        if product:
            product.quantity += item.quantity
            self.notify(
                {
                    "action": "add_stock",
                    "item": item,
                    "update": item.quantity,
                    "quantity": product.quantity,
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
                {"action": "remove_item", "item": product, "quantity": product.quantity}
            )
        else:
            return None

    def find_item(self, code):
        for item in self.items:
            if item.code == code:
                return item
        return None

    def update_stock(self, code, quantity):
        product = self.find_item(code)
        if product and quantity > 0:
            product.quantity += quantity
            self.notify(
                {
                    "action": "add_stock",
                    "item": product,
                    "update": quantity,
                    "quantity": product.quantity,
                }
            )
        elif product and quantity < 0:
            product.quantity += quantity
            self.notify(
                {
                    "action": "minus_stock",
                    "item": product,
                    "update": quantity,
                    "quantity": product.quantity,
                }
            )
        else:
            return

    def add_observer(self, observer: "Observer"):
        self.observers.append(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)

    def display_inventory(self):
        self.inventoryviewer.display_inventory()

    def set_threshold(self, threshold):
        self.threshold = threshold

    def is_low_stock(self, quantity):
        return quantity <= self.threshold

    def stock_warning(self):
        for item in self.items:
            if self.is_low_stock(item.quantity):
                self.notify(
                    {
                        "action": "low_stock_warning",
                        "item": item,
                        "quantity": item.quantity,
                    }
                )

    def display_logger(self):
        for observer in self.observers:
            if isinstance(observer, Logger):
                viewer = ObserverViewer(observer)
                viewer.display_records()

    def display_stockalert(self):
        for observer in self.observers:
            if isinstance(observer, StockAlertSystem):
                viewer = ObserverViewer(observer)
                viewer.display_records()

    def display_records(self):
        self.display_logger()
        self.display_stockalert()


class FoodMenuInventory(Inventory):
    pass


class IngredientInventory(Inventory):
    pass


class BeverageInventory(Inventory):
    pass


class InventoryViewer:
    def __init__(self, inventory: Inventory):
        self.inventory = inventory

    def display_inventory(self):
        for item in self.inventory.items:
            print(item.get_details())


class Store:
    def __init__(self):
        self.inventories = {
            "food": FoodMenuInventory(),
            "beverage": BeverageInventory(),
            "ingredient": IngredientInventory(),
        }
        self.current_inventory = None
        self.logger = Logger()
        self.stockalert = StockAlertSystem()

        for key in self.inventories:
            self.inventories[key].add_observer(self.logger)
            self.inventories[key].add_observer(self.stockalert)

    def set_inventory(self, inventory_type):
        if inventory_type in self.inventories:
            self.current_inventory = self.inventories[inventory_type]
        else:
            raise RuntimeError("Error")

    def add_item(self, item):
        self.current_inventory.add_item(item)

    def remove_item(self, code):
        self.current_inventory.remove_item(code)

    def find_item(self, code):
        return self.current_inventory.find_item(code)

    def update_stock(self, code, quantity):
        self.current_inventory.update_stock(code, quantity)

    def display_inventory(self):
        self.current_inventory.display_inventory()


class Observer(ABC):
    def __init__(self):
        self.records = []

    @abstractmethod
    def update(self, message):
        pass


class Logger(Observer):
    def update(self, message):
        if message["action"] == "add_item":
            item = message["item"]
            quantity = message["quantity"]
            record = f"Added Item : {item.name} Quantity : {quantity}"
            self.records.append(record)
        elif message["action"] == "remove_item":
            item = message["item"]
            quantity = message["quantity"]
            record = f"Removed Item : {item.name} Quantity : {quantity}"
            self.records.append(record)
        else:
            return None


class StockAlertSystem(Observer):
    def update(self, message):
        action = message.get("action")
        item = message.get("item")
        quantity = message.get("quantity")
        update = message.get("update")

        templates = {
            "add_stock": f"Add Stock : {item.name} Added Qtty : {quantity} Total : {quantity}",
            "minus_stock": f"Minus Stock : {item.name} difference {update} Total : {quantity}",
            "low-warning": f"low_stock_warning : {item.name} Quantity : {quantity}",
        }

        record = templates.get(action)
        if record:
            self.records.append(record)


class ObserverViewer:
    def __init__(self, observer: Observer):
        self.observer = observer

    def display_records(self):
        print(f"< -- Observer type : {type(self.observer).__name__} -->")
        if not hasattr(self.observer, "records") or not self.observer.records:
            print("Doesn't have records")
            return

        for idx, record in enumerate(self.observer.records):
            print("< Records ---> records")
