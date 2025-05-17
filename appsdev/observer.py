from abc import ABC, abstractmethod


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
        elif message["action"] == "removed_item":
            item = message["item"]
            quantity = message["quantity"]
            record = f"Removed Item : {item.name} Quantity : {quantity}"
            self.records.append(record)
        else:
            return None


class StockAlertSystem(Observer):
    def __init__(self):
        self.records = []

    def update(self, message):
        action = message.get("action")
        item = message.get("item")
        quantity = message.get("quantity")
        update = message.get("update")
        total = message.get("total")

        templates = {
            "add_stock": f"Add Stock : {item.name} Added Qtty : {quantity} Total : {total}",
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
        for record in self.observer.records:
            print(record)
