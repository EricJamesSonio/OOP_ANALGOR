from abc import ABC, abstractmethod
from typing import List, Optional


class StoreItem:
    def __init__(self, name, code, price, quantity):
        self.name = name
        self.code = code
        self.price = price
        self.quantity = quantity


class Screw(StoreItem):
    def __init__(self, name, code, price, quantity):
        super().__init__(name, code, price, quantity)


class Hammer(StoreItem):
    def __init__(self, name, code, price, quantity):
        super().__init__(name, code, price, quantity)


class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass


class Logger(Observer):
    def update(self, message):
        if message["action"] == "new_item":
            item = message["item"]
            quantity = message["quantity"]
            return f"New item : {item.name} qtty : {quantity} was added!"
        elif message["action"] == "add_stock":
            return None


class AlertSystem(Observer):
    def update(self, message):
        if message["action"] == "add_stock":
            item = message["item"]
            quantity = message["quantity"]
            return f"Added stock qtty : {quantity} to {item.name} was added!"


class StockManager:
    def __init__(self):
        self.items: List["StoreItem"] = []
        self.observers: List["Observer"] = []

    def add_item(self, item, quantity):
        for existing_item in self.items:
            if existing_item.code == item.code:
                existing_item.quantity += quantity
                self.notify({"action": "add_stock", "item": item, "quantity": quantity})
                return
        item.quantity = quantity
        self.items.append(item)
        self.notify({"action": "new_item", "item": item, "quantity": quantity})

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify(self, message):
        for obs in self.observers:
            response = obs.update(message)
            if response:
                print(response)

    def display(self):
        for item in self.items:
            print(f"item : {item.name}, Quantity : {item.quantity}")


def main():
    stock = StockManager()

    logger = Logger()
    alert = AlertSystem()
    stock.add_observer(logger)
    stock.add_observer(alert)

    screw = Screw("Screw", 101, 1.5, 0)
    hammer = Hammer("Hammer", 102, 8.0, 0)

    stock.add_item(screw, 100)
    stock.add_item(hammer, 50)

    stock.add_item(screw, 50)

    stock.display()


if __name__ == "__main__":
    main()
